project(simulators)

if (NOT BUILD_SIM)
  message("[RND][SIM] disabled")
  return()
endif()

set(SIM_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

# Include simulator cmakes
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/spike.cmake")
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/qemu.cmake")

# Build all simulators only if proper option is set
if (BUILD_SIM)
  set(CUR_AVAILABLE_SIM ${AVAILABLE_SIM})

  # Build spike target and report it's enabled
  set(G_PREFIX_SIM_SPIKE ${CMAKE_INSTALL_PREFIX}/spike)
  build_sim_spike(${G_PREFIX_SIM_SPIKE} "")
  list(APPEND CUR_AVAILABLE_SIM "SPIKE")

  # Build qemu target and report it's enabled
  set(G_PREFIX_SIM_QEMU ${CMAKE_INSTALL_PREFIX}/qemu)
  build_sim_qemu(${G_PREFIX_SIM_QEMU} "")
  list(APPEND CUR_AVAILABLE_SIM "QEMU")

  # Update variable with available simulators in parent scope
  message("[RND][SIM] enabled - ${CUR_AVAILABLE_SIM}")
  set(AVAILABLE_SIM ${CUR_AVAILABLE_SIM} PARENT_SCOPE)
endif (BUILD_SIM)
