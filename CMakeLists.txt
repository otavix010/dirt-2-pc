# dirt2 - ReXGlue Recompiled Project
#
# SDK boilerplate lives in generated/rexglue.cmake.

cmake_minimum_required(VERSION 3.25)
project(dirt2 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(generated/rexglue.cmake)

# Sources
set(DIRT2_SOURCES
    src/main.cpp
)

if(WIN32)
    add_executable(dirt2 WIN32 ${DIRT2_SOURCES})
else()
    add_executable(dirt2 ${DIRT2_SOURCES})
endif()

rexglue_setup_target(dirt2 GPU_PLUGINS xenos)

# the ports' common part: linker map, -march=native on the player's PC, the FidelityFX runtime (port.cmake)
include(port.cmake)
port_setup(dirt2)
