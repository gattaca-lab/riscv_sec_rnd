from distutils.dir_util import copy_tree
from pathlib import Path
import glob
import logging as log
import os

from .basic_builder import BasicBuilder

class Builder_C(BasicBuilder):
  def __init__(self, CFG, platforms):
    super().__init__(CFG, platforms)
    self.name = "c"
    log.debug("builder <C> initialized")

  def prepair(self, testInfo):
    TestName = testInfo.name()
    Platform = testInfo.platform()
    log.debug("<C> Builder prepair test <{}> in {}".format(TestName, testInfo.wd()))
    log.debug("   test <{}> src: {}".format(TestName, testInfo.src()))
    log.debug("   test <{}> coping sources to: {}".format(TestName, testInfo.wd()))
    copy_tree(testInfo.src(), testInfo.wd())

    pcwd = os.getcwd()
    os.chdir(testInfo.wd())
    Sources = [f"\"{str(s)}\"" for s in glob.glob("**.c")]
    os.chdir(pcwd)

    # copy platform configuration files
    # create list of sources
    # render makefile
    test_binary = "test.elf"
    log.debug(self.cfg)
    KV = {
      "@platform_compiler" : "gcc",
      "@platform_cflags" : [],
      "@test_binary" : test_binary,
      "@src_files" : Sources,
      "@run_string" : "build/test.elf"
    }
    self.renderMakefile(testInfo.wd(), KV, "makefile_c.erb")
    return testInfo

