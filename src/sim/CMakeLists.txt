project(simulators)

set(SIM_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

# Include simulator cmakes
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/spike.cmake")
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/qemu.cmake")

# Build all simulators only if proper option is set
if (BUILD_SIM)
  set(CUR_AVAILABLE_SIM ${AVAILABLE_SIM})
  # Build spike target and report it's enabled
  build_sim_spike("")
  list(APPEND CUR_AVAILABLE_SIM "SPIKE")

  # Build qemu target and report it's enabled
  build_sim_qemu("")
  list(APPEND CUR_AVAILABLE_SIM "QEMU")
  # Update variable with available simulators in parent scope
  set(AVAILABLE_SIM ${CUR_AVAILABLE_SIM} PARENT_SCOPE)
endif (BUILD_SIM)
