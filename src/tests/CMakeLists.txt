project(tests)

add_subdirectory(config)

set(TEST_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

# Include tests cmakes
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/dummy.cmake")

# Build a dummy test
build_tests_dummy("")
