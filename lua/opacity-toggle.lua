-- ============================================================
--  wezext 扩展示例（纯 Lua，没有可执行文件）
--
--  契约：返回一个 function(config, wezterm)，wezext 生成的
--        ~/.wezterm-ext.lua 会把它放进 apply 列表，主配置逐个调用。
--  作用：Ctrl+Shift+Y 在不透明 / 半透明之间切换当前窗口。
-- ============================================================
return function(config, wezterm)
  config.keys = config.keys or {}

  local OPAQUE = 1.0
  local TRANSLUCENT = 0.45

  config.keys[#config.keys + 1] = {
    key = 'y',
    mods = 'CTRL|SHIFT',
    action = wezterm.action_callback(function(window, pane)
      local overrides = window:get_config_overrides() or {}
      local current = overrides.window_background_opacity
      if current == nil then
        current = OPAQUE
      end
      if current >= OPAQUE then
        overrides.window_background_opacity = TRANSLUCENT
      else
        overrides.window_background_opacity = OPAQUE
      end
      window:set_config_overrides(overrides)
    end),
  }
end
