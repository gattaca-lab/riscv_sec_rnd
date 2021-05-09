cmake_minimum_required(VERSION 3.10)
project(RISC-V_Security_RnD)

# Options
option(BUILD_SIM "BUILD_SIM" ON)
option(BUILD_TOOLCHAIN "BUILD_TOOLCHAIN" ON)

set(AVAILABLE_SIM "")
set(AVAILABLE_TOOLCHAIN "")

#include simulators
add_subdirectory(sim)
#include toolchains
add_subdirectory(toolchain)
#include tests
add_subdirectory(tests)
