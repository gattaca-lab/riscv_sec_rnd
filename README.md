# RISC-V Security R&D project home  
This is home for updated risc-v security project.  

# Available cmake options  
- **CMAKE_INSTALL_PREFIX**=\<path\> - specifies install path for components
- **BUILD_SIM**=ON/OFF - enables or disables building simulators  
- **BUILD_TOOLCHAIN**=ON/OFF - enables or disables building toolchains  

# How to build
```
git clone https://github.com/gattaca-lab/riscv_sec_rnd && cd riscv_sec_rnd
git submodule update --init --remote
mkdir tmp && cd tmp
cmake ../ -CMAKE_INSTALL_PREFIX=<path>
make
```
