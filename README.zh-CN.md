# wezext-index

[English](README.md) | **中文**

[wezext](https://github.com/wezext-community/wezext) 的扩展索引。

* `index/<name>.json` —— 每个扩展一个文件（**改这里**）
* `index.json` —— 由脚本聚合生成，供 `wezext` 读取（**不要手改**）

新增扩展：加一个 `index/<name>.json` → 跑 `python tools/gen-index.py` → 两个文件一起提交。

## 索引项格式

```json
{
  "name": "wezfont",
  "display": "wezfont 字体选择器",
  "description": "一句话说明。",
  "version": "0.1.0",
  "homepage": "https://github.com/wezext-community/wezfont",
  "source": { "repo": "https://github.com/wezext-community/wezfont", "crate": "wezfont" },
  "binary": {
    "asset": "wezfont-v{version}-x86_64-pc-windows-msvc.zip",
    "exe": "wezfont.exe",
    "url": "https://github.com/wezext-community/wezfont/releases/download/v{version}/{asset}",
    "sha256": "可选，填了就强制校验"
  },
  "lua": "https://example.com/ext/foo.lua",
  "keys": [{ "key": "f", "mods": "CTRL|SHIFT", "args": [], "hint": "这个键干什么" }]
}
```

| 字段 | 含义 |
| --- | --- |
| `binary` | 预编译 zip，里面要有 `exe` 指定的文件；`url` 里的 `{version}` / `{asset}` 会被替换 |
| `source` | 从 `repo` 做 `git clone` + `cargo build --release`（优先 tag `v<version>`，失败退回默认分支） |
| `lua` | Lua 片段文件，内容必须 `return function(config, wezterm) ... end` |
| `keys` | 生成到 `~/.wezterm-ext.lua`，动作是"开新标签页运行这个 exe" |

`binary` / `source` / `lua` 至少要有一个；`keys` 可选。

## 校验

```bash
python tools/gen-index.py    # 条目不合法时拒绝写出
```
