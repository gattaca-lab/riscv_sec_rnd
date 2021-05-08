include(ExternalProject)
include(ProcessorCount)
ProcessorCount(N)

# Qemu related varuables
set(QEMU_SRC_DIR "${SIM_SRC_DIR}/qemu/")
set(QEMU_INSTALL_DIR "${INSTALL_DIR}/qemu/")

# Function to build qemu simulator
function(build_sim_qemu EXTRA_CONFIG_ARGS)
  # Create build and install directories
  file(MAKE_DIRECTORY ${QEMU_INSTALL_DIR})
  ExternalProject_Add(
      qemu
      PREFIX ${QEMU_INSTALL_DIR}
      SOURCE_DIR ${QEMU_SRC_DIR}
      CONFIGURE_COMMAND ${QEMU_SRC_DIR}/configure --prefix=${QEMU_INSTALL_DIR} --target-list=riscv32-softmmu,riscv64-softmmu,riscv32-linux-user,riscv64-linux-user ${EXTRA_CONFIG_ARGS}
      BUILD_COMMAND make -j${N}
      INSTALL_COMMAND make install -j${N}
  )
endfunction()
