project(simulators)

set(SIM_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

# Include simulator cmakes
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/spike.cmake")
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/qemu.cmake")

# Build all simulators only if proper option is set
if (BUILD_SIM)
  build_sim_spike("")
  build_sim_qemu("")
endif (BUILD_SIM)
