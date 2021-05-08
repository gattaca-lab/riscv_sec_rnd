project(simulators)

set(SIM_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

# Include simulator cmakes
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/spike.cmake")
