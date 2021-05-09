if (BUILD_SIM)
  ExternalProject_Get_Property(qemu INSTALL_DIR)
  set(PREFIX_SIM_QEMU ${INSTALL_DIR})

  ExternalProject_Get_Property(spike INSTALL_DIR)
  set(PREFIX_SIM_SPIKE ${INSTALL_DIR})
endif(BUILD_SIM)

if (BUILD_TOOLCHAIN)
  ExternalProject_Get_Property(gcc_rv32i_newlib INSTALL_DIR)
  set(PREFIX_TOOLCHAIN_GCC_RV32I_NEWLIB ${INSTALL_DIR})

  ExternalProject_Get_Property(gcc_rv32imc_newlib INSTALL_DIR)
  set(PREFIX_TOOLCHAIN_GCC_RV32IMC_NEWLIB ${INSTALL_DIR})
endif()

message("qemu: ${PREFIX_SIM_QEMU}")
message("spike: ${PREFIX_SIM_SPIKE}")
message("gcc32_i: ${PREFIX_TOOLCHAIN_GCC_RV32I_NEWLIB}")
message("gcc32_imc: ${PREFIX_TOOLCHAIN_GCC_RV32IMC_NEWLIB}")
configure_file(config.in config.yaml)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/config.yaml DESTINATION share)
