require 'erb'

@src_files = [
  "main.c",
  "depend.c"
]
@platform_include = "include.makefile"
@run_string = "fsim test.elf"
@test_binary = "test.elf"
@platform_compiler = "gcc"
@platform_cflags = ["-march=rv32i"]
TemplateString  = File.read("makefile_c.erb")
print ERB.new(TemplateString).result(binding)
