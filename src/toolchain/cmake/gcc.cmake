include(ExternalProject)
include(ProcessorCount)
ProcessorCount(N)

# Gcc toolchain related varuables
set(GCC_SRC_DIR "${TOOLCHAIN_SRC_DIR}/gcc")

# Function to build gcc toolchain for rv32i_newlib target
function(build_toolchain_rv32i_newlib GCC_INSTALL_DIR EXTRA_CONFIG_ARGS)
  # Create build and install directories
  file(MAKE_DIRECTORY ${GCC_INSTALL_DIR})
  ExternalProject_Add(
      gcc_rv32i_newlib
      PREFIX ${GCC_INSTALL_DIR}
      SOURCE_DIR ${GCC_SRC_DIR}
      CONFIGURE_COMMAND ${GCC_SRC_DIR}/configure --with-arch=rv32i
                        --prefix=${GCC_INSTALL_DIR}
                        ${EXTRA_CONFIG_ARGS}
      BUILD_COMMAND make -j${N} && make clean
  )
endfunction()

# Function to build gcc toolchain for rv32imc_newlib target
function(build_toolchain_rv32imc_newlib GCC_INSTALL_DIR EXTRA_CONFIG_ARGS)
  # Create build and install directories
  file(MAKE_DIRECTORY ${GCC_INSTALL_DIR})
  ExternalProject_Add(
      gcc_rv32imc_newlib
      PREFIX ${GCC_INSTALL_DIR}
      SOURCE_DIR ${GCC_SRC_DIR}
      CONFIGURE_COMMAND ${GCC_SRC_DIR}/configure --with-arch=rv32imc
                        --prefix=${GCC_INSTALL_DIR}
                        ${EXTRA_CONFIG_ARGS}
      BUILD_COMMAND make -j${N} && make clean
  )
endfunction()
