// dirt2 - ReXGlue Recompiled Project
//
// The port's app: the common base of the Xbox 360 ports (port/port_app.h) and DiRT 2's own hooks: the utility drive
// (cache:), where the game keeps its replays and flashbacks.

#pragma once

#include <rex/hook.h>

#include "port/port_app.h"

// XMountUtilityDrive(format_clean, bytes_per_cluster, file_cache_size), the XAPI's, linked into the game and called by
// sub_823F5328 with (1, 0x8000, 0): the drive as a folder (port/cache_drive.h), ERROR_SUCCESS
REX_HOOK_RAW(sub_829D0BC0) {
  (void)base;
  ctx.r3.u64 = port::MountCacheDrive() ? 0 : 1;
}

class Dirt2App : public PortApp {
 public:
  using PortApp::PortApp;

  static std::unique_ptr<rex::ui::WindowedApp> Create(rex::ui::WindowedAppContext& ctx) {
    crash_log::Install();
    return std::unique_ptr<Dirt2App>(new Dirt2App(ctx, "dirt2", PPCImageConfig));
  }
};
