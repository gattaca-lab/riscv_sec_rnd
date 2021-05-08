project(toolchains)

set(TOOLCHAIN_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

# Include toolchain cmakes
#include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/gcc.cmake")

# Build all toolchains only if proper option is set
if (BUILD_TOOLCHAIN)
  build_toolchain_rv32i("")
  build_toolchain_rv32imc("")
endif (BUILD_TOOLCHAIN)
