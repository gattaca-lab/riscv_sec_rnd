cmake_minimum_required(VERSION 3.10)
project(RISC-V_Security_RnD)

# Process install directory
if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  message(FATAL_ERROR "Please set CMAKE_INSTALL_PREFIX variable")
else(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set(INSTALL_DIR "${CMAKE_INSTALL_PREFIX}")
  file(MAKE_DIRECTORY ${INSTALL_DIR})
endif(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)

# Options
option(BUILD_SIM "BUILD_SIM" ON)
option(BUILD_TOOLCHAIN "BUILD_TOOLCHAIN" ON)

set(AVAILABLE_SIM "")
set(AVAILABLE_TOOLCHAIN "")

### Includes
#include simulators
add_subdirectory("${CMAKE_SOURCE_DIR}/src/sim/")
#include toolchains
add_subdirectory("${CMAKE_SOURCE_DIR}/src/toolchain/")
