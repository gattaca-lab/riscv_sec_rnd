project(toolchains)

set(TOOLCHAIN_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

# Include toolchain cmakes
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/gcc.cmake")

# Build all toolchains only if proper option is set
if (BUILD_TOOLCHAIN)
  set(CUR_AVAILABLE_TOOLCHAIN ${AVAILABLE_TOOLCHAIN})
  # Build spike target and report it's enabled
  build_toolchain_rv32i_newlib("")
  list(APPEND CUR_AVAILABLE_TOOLCHAIN "GCC_RV32I_NEWLIB")

  # Build spike target and report it's enabled
  build_toolchain_rv32imc_newlib("")
  list(APPEND CUR_AVAILABLE_TOOLCHAIN "GCC_RV32IMC_NEWLIB")
  # Update variable with available simulators in parent scope
  set(AVAILABLE_TOOLCHAIN ${CUR_AVAILABLE_TOOLCHAIN} PARENT_SCOPE)
endif (BUILD_TOOLCHAIN)
