-- ============================================================
--  wezext extension example (pure Lua, no executable)
--
--  Contract: return a function(config, wezterm). wezext puts it into the
--  generated ~/.wezterm-ext.lua, and the main config calls each of them.
--
--  What it does: Ctrl+Shift+Y toggles the current window between opaque
--  and translucent.
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
