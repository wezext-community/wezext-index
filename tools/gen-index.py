#!/usr/bin/env python3
"""把 index/*.json 合并成 index.json（单文件聚合，供 wezext 一次性拉取）。

用法：  python tools/gen-index.py
输出：  index.json
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX_DIR = ROOT / "index"
OUT = ROOT / "index.json"

REQUIRED = ("name", "version", "description")


def main() -> int:
    extensions = {}
    errors = []

    for path in sorted(INDEX_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{path.name}: JSON 解析失败: {e}")
            continue

        missing = [k for k in REQUIRED if not data.get(k)]
        if missing:
            errors.append(f"{path.name}: 缺少字段 {', '.join(missing)}")
            continue

        name = data["name"]
        if name in extensions:
            errors.append(f"{path.name}: 扩展名 {name} 重复")
            continue
        if path.stem != name:
            errors.append(f"{path.name}: 文件名应与 name 一致（期望 {name}.json）")
            continue

        has_source = isinstance(data.get("source"), dict)
        has_binary = isinstance(data.get("binary"), dict)
        has_lua = bool(data.get("lua"))
        if not (has_source or has_binary or has_lua):
            errors.append(f"{path.name}: 至少要有 source / binary / lua 其中一项")
            continue

        for key in data.get("keys", []):
            if not key.get("key"):
                errors.append(f"{path.name}: keys 里有条目缺少 key")
                break
            key.setdefault("mods", "NONE")
            key.setdefault("args", [])

        extensions[name] = data

    if errors:
        for e in errors:
            print(f"ERROR  {e}", file=sys.stderr)
        return 1

    out = {
        "schema": 1,
        "generated_by": "tools/gen-index.py",
        "extensions": dict(sorted(extensions.items())),
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.name}: {len(extensions)} 个扩展 -> {', '.join(out['extensions'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
