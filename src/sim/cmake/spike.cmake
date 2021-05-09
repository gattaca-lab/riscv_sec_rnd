include(ExternalProject)
include(ProcessorCount)
ProcessorCount(N)

# Spike related varuables
set(SPIKE_SRC_DIR "${SIM_SRC_DIR}/spike")
set(SPIKE_INSTALL_DIR "${INSTALL_DIR}/spike")

# Function to build spike simulator
function(build_sim_spike EXTRA_CONFIG_ARGS)
  # Create build and install directories
  file(MAKE_DIRECTORY ${SPIKE_INSTALL_DIR})
  ExternalProject_Add(
      spike
      PREFIX ${SPIKE_INSTALL_DIR}
      SOURCE_DIR ${SPIKE_SRC_DIR}
      CONFIGURE_COMMAND ${SPIKE_SRC_DIR}/configure --prefix=${SPIKE_INSTALL_DIR}
          ${EXTRA_CONFIG_ARGS}
      BUILD_COMMAND make -j${N}
      INSTALL_COMMAND make install -j${N}
  )
endfunction()
