# wezext-index

**English** | [中文](README.zh-CN.md)

The extension index for [wezext](https://github.com/wezext-community/wezext).

* `index/<name>.json` — one file per extension (**edit these**)
* `index.json` — generated aggregate read by `wezext` (**do not edit by hand**)

Adding an extension: drop `index/<name>.json`, run `python tools/gen-index.py`,
and commit both files.

## Entry format

```json
{
  "name": "wezfont",
  "display": "wezfont font picker",
  "description": "One-line description.",
  "version": "0.1.0",
  "homepage": "https://github.com/wezext-community/wezfont",
  "source": { "repo": "https://github.com/wezext-community/wezfont", "crate": "wezfont" },
  "binary": {
    "asset": "wezfont-v{version}-x86_64-pc-windows-msvc.zip",
    "exe": "wezfont.exe",
    "url": "https://github.com/wezext-community/wezfont/releases/download/v{version}/{asset}",
    "sha256": "optional; verified when present"
  },
  "lua": "https://example.com/ext/foo.lua",
  "keys": [{ "key": "f", "mods": "CTRL|SHIFT", "args": [], "hint": "what it does" }]
}
```

| Field | Meaning |
| --- | --- |
| `binary` | prebuilt zip containing `exe`; `{version}` / `{asset}` are substituted into `url` |
| `source` | `git clone` + `cargo build --release` from `repo` (tag `v<version>`, falls back to default branch) |
| `lua` | a Lua file that must `return function(config, wezterm) ... end` |
| `keys` | written into `~/.wezterm-ext.lua` as "open a new tab running this exe" |

At least one of `binary` / `source` / `lua` is required. `keys` is optional.

## Validate

```bash
python tools/gen-index.py    # refuses to write when entries are invalid
```
