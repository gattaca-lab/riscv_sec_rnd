project(toolchains)

if (NOT BUILD_TOOLCHAIN)
  message("[RND][TOOLCHAIN] disabled")
  return()
endif()

set(TOOLCHAIN_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

set(TOOLCHAINS_INSTALL_ROOT "${CMAKE_INSTALL_PREFIX}/toolchains"
    CACHE INTERNAL "TOOLCHAINS_INSTALL_ROOT" FORCE)

# Include toolchain cmakes
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/gcc.cmake")

# Build all toolchains only if proper option is set
if (BUILD_TOOLCHAIN)
  set(CUR_AVAILABLE_TOOLCHAIN ${AVAILABLE_TOOLCHAIN})
  # Build spike target and report it's enabled
  set(G_PREFIX_TOOLCHAIN_GCC_RV32I_NEWLIB ${TOOLCHAINS_INSTALL_ROOT}/riscv32i_newlib)
  build_toolchain_rv32i_newlib(${G_PREFIX_TOOLCHAIN_GCC_RV32I_NEWLIB} "")
  list(APPEND CUR_AVAILABLE_TOOLCHAIN "GCC_RV32I_NEWLIB")

  # Build spike target and report it's enabled
  set(G_PREFIX_TOOLCHAIN_GCC_RV32IMC_NEWLIB ${TOOLCHAINS_INSTALL_ROOT}/riscv32imc_newlib)
  build_toolchain_rv32imc_newlib(${G_PREFIX_TOOLCHAIN_GCC_RV32IMC_NEWLIB} "")
  list(APPEND CUR_AVAILABLE_TOOLCHAIN "GCC_RV32IMC_NEWLIB")

  # Update variable with available simulators in parent scope
  message("[RND][TOOLCHAIN] enabled: ${CUR_AVAILABLE_TOOLCHAIN}")
  set(AVAILABLE_TOOLCHAIN ${CUR_AVAILABLE_TOOLCHAIN} PARENT_SCOPE)
endif (BUILD_TOOLCHAIN)
