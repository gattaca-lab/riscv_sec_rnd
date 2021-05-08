enable_testing()

# Dummy test related varuables
set(DUMMY_SRC_DIR "${TEST_SRC_DIR}/dummy/")
set(DUMMY_INSTALL_DIR "${INSTALL_DIR}/tests/dummy/")

#FIXME: no access to GCC_INSTALL
set(COMPILER_BIN "${GCC_INSTALL_DIR}/riscv32i_newlib/bin/riscv32-unknown-elf-gcc")

function(BUILD_TESTS_DUMMY EXTRA_ARGS)
  add_test(dummy_test ${COMPILER_BIN} "${DUMMY_SRC_DIR}/main.c")
endfunction()
