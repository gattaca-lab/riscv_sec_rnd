include(ExternalProject)
include(ProcessorCount)
ProcessorCount(N)

# Gcc toolchain related varuables
set(GCC_SRC_DIR "${TOOLCHAIN_SRC_DIR}/gcc/")
# FIXME: ultra ugly hack
set(GCC_INSTALL_DIR "${INSTALL_DIR}/toolchains/" CACHE INTERNAL "GCC_INSTALL_DIR" FORCE)

# Function to build gcc toolchain for rv32i_newlib target
function(build_toolchain_rv32i_newlib EXTRA_CONFIG_ARGS)
  set(GCC_RV32I_NEWLIB_INSTALL_DIR "${GCC_INSTALL_DIR}/riscv32i_newlib/")

  # Create build and install directories
  file(MAKE_DIRECTORY ${GCC_RV32I_NEWLIB_INSTALL_DIR})
  ExternalProject_Add(
      gcc_rv32i_newlib
      PREFIX ${GCC_RV32I_NEWLIB_INSTALL_DIR}
      SOURCE_DIR ${GCC_SRC_DIR}
      CONFIGURE_COMMAND ${GCC_SRC_DIR}/configure --with-arch=rv32i --prefix=${GCC_RV32I_NEWLIB_INSTALL_DIR} ${EXTRA_CONFIG_ARGS}
      BUILD_COMMAND make -j${N} && make clean
  )
endfunction()

# Function to build gcc toolchain for rv32imc_newlib target
function(build_toolchain_rv32imc_newlib EXTRA_CONFIG_ARGS)
  set(GCC_RV32IMC_NEWLIB_INSTALL_DIR "${GCC_INSTALL_DIR}/riscv32imc_newlib/")

  # Create build and install directories
  file(MAKE_DIRECTORY ${GCC_RV32IMC_NEWLIB_INSTALL_DIR})
  ExternalProject_Add(
      gcc_rv32imc_newlib
      PREFIX ${GCC_RV32IMC_NEWLIB_INSTALL_DIR}
      SOURCE_DIR ${GCC_SRC_DIR}
      CONFIGURE_COMMAND ${GCC_SRC_DIR}/configure --with-arch=rv32imc --prefix=${GCC_RV32IMC_NEWLIB_INSTALL_DIR} ${EXTRA_CONFIG_ARGS}
      BUILD_COMMAND make -j${N} && make clean
  )
endfunction()
