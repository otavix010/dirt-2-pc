// dirt2 - ReXGlue Recompiled Project
//
// The port's app: the common base of the Xbox 360 ports (port/port_app.h) and DiRT 2's own hooks.

#pragma once

#include "port/port_app.h"

class Dirt2App : public PortApp {
 public:
  using PortApp::PortApp;

  static std::unique_ptr<rex::ui::WindowedApp> Create(rex::ui::WindowedAppContext& ctx) {
    crash_log::Install();
    return std::unique_ptr<Dirt2App>(new Dirt2App(ctx, "dirt2", PPCImageConfig));
  }
};
