"""Regenerate skills/gramgpt/references/tools/*.md from the live public OpenAPI.

    python3 scripts/gen_reference.py            # from https://gramgpt.io
    python3 scripts/gen_reference.py spec.json  # from a saved spec

Stdlib only. Run weekly by .github/workflows/refresh.yml.
"""
import json
import pathlib
import sys
import urllib.request

SPEC_URL = "https://gramgpt.io/api/v1/openapi.json?format=json"
OUT = pathlib.Path(__file__).resolve().parent.parent / "skills/gramgpt/references/tools"
TOOL_PREFIX = "/api/v1/tools/"
LAUNCH_OPTIONS = {"dry_run", "skip_unavailable", "queue_if_busy", "strict_config", "tags", "external_id"}


def load_spec(src: str | None) -> dict:
    if src:
        return json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
    req = urllib.request.Request(SPEC_URL, headers={"Accept-Language": "en", "User-Agent": "gramgpt-claude-plugin"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def one_line(text) -> str:
    return " ".join(str(text or "").split()).replace("|", "\\|")


def type_of(s: dict) -> str:
    if "enum" in s:
        return " \\| ".join(f"`{v}`" for v in s["enum"])
    t = s.get("type", "any")
    if t == "array":
        return f"{type_of(s.get('items', {}))}[]"
    return t


def limits(s: dict) -> str:
    parts = []
    for k, label in (("default", "default"), ("minimum", "min"), ("maximum", "max"),
                     ("minItems", "min items"), ("maxItems", "max items"), ("maxLength", "max len")):
        if k in s:
            parts.append(f"{label} `{json.dumps(s[k], ensure_ascii=False)}`")
    return ", ".join(parts)


def table(props: dict, required: set) -> list[str]:
    rows = ["| field | type | | notes |", "|---|---|---|---|"]
    for name, s in props.items():
        note = "; ".join(x for x in (one_line(s.get("description")), limits(s)) if x)
        rows.append(f"| `{name}` | {type_of(s)} | {'**required**' if name in required else ''} | {note} |")
    return rows


def render(name: str, op: dict) -> str:
    schema = op["requestBody"]["content"]["application/json"]["schema"]
    props = dict(schema.get("properties") or {})
    required = set(schema.get("required") or [])
    config = props.pop("config", None)
    options = props.pop("options", None)
    common = LAUNCH_OPTIONS <= props.keys()
    if common:
        for k in LAUNCH_OPTIONS:
            props.pop(k)
    out = [f"# {name}", "", one_line(op.get("summary")), ""]
    if common:
        out += ["Also takes the common launch options — `dry_run`, `skip_unavailable`, "
                "`queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).", ""]
    if op.get("description") and one_line(op["description"]) != one_line(op.get("summary")):
        out += [op["description"].strip(), ""]
    if props:
        out += ["## Input", ""] + table(props, required) + [""]
    if config and config.get("properties"):
        out += ["## config", "", one_line(config.get("description")), ""]
        out += table(config["properties"], set(config.get("required") or [])) + [""]
    if options and options.get("properties"):
        out += ["## options", ""] + table(options["properties"], set()) + [""]
    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    spec = load_spec(sys.argv[1] if len(sys.argv) > 1 else None)
    tools = {
        path[len(TOOL_PREFIX):].strip("/"): item["post"]
        for path, item in spec["paths"].items()
        if path.startswith(TOOL_PREFIX) and "post" in item and path != TOOL_PREFIX
    }
    assert len(tools) > 20, f"suspiciously few tools in spec: {len(tools)}"
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.md"):
        if old.stem not in tools:
            old.unlink()
    for name, op in sorted(tools.items()):
        (OUT / f"{name}.md").write_text(render(name, op), encoding="utf-8")
    print(f"{len(tools)} tools → {OUT}")


if __name__ == "__main__":
    main()
