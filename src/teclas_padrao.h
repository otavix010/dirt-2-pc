// The game's own keys for keyboard and mouse (port/port_app.h applies them to the engine's keybind_* options,
// where the player left them alone). The same defaults as the game's profile in the Otavix Launcher.
// Written by teclas_360.py: the table of the four ports is there.

#pragma once

inline constexpr const char* kPortKeys =
    "lstick_up=;lstick_down=;lstick_left=a;lstick_right=d;a=space enter;b=e backspace;x=q;y=c;left_shoulder=lctrl;right_shoulder=lshift;left_trigger=s;right_trigger=w;start=escape;back=tab;dpad_up=up;dpad_down=down;dpad_left=left;dpad_right=right;rstick_up=num8;rstick_down=num2;rstick_left=num4;rstick_right=num6;lstick_press=z;rstick_press=x";
inline constexpr bool kPortMouse = false;
inline constexpr int kPortMouseSensitivity = 50;  // percent
