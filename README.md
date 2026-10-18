# wezext-index

[wezext](https://github.com/wezext-community/wezext) 的扩展索引。

- `index/<name>.json` —— 每个扩展一个文件（**改这里**）
- `index.json` —— 由 `tools/gen-index.py` 聚合生成（**不要手改**）
- 新增扩展：加 `index/<name>.json` → 跑 `python tools/gen-index.py` → 提交

## 索引项字段

```json
{
  "name": "wezfont",
  "display": "显示名",
  "description": "一句话说明",
  "version": "0.1.0",
  "homepage": "https://github.com/...",
  "source": { "repo": "https://github.com/...", "crate": "wezfont" },
  "binary": {
    "asset": "wezfont-v{version}-x86_64-pc-windows-msvc.zip",
    "exe": "wezfont.exe",
    "url": "https://github.com/.../releases/download/v{version}/{asset}",
    "sha256": "可选，填了就强制校验"
  },
  "lua": "https://.../ext/foo.lua",
  "keys": [ { "key": "f", "mods": "CTRL|SHIFT", "args": [], "hint": "..." } ]
}
```

- `binary`：预编译 zip（里面要有 `exe` 那个文件）
- `source`：源码构建（`cargo build --release`）
- `lua`：纯 Lua 片段，文件里要 `return function(config, wezterm) ... end`
- `keys`：wezext 会生成到 `~/.wezterm-ext.lua`，键位动作是「开新标签页运行这个 exe」
