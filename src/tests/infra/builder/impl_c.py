import logging as log
from distutils.dir_util import copy_tree
import os

from .basic_builder import BasicBuilder

class Builder_C(BasicBuilder):
  def __init__(self, CFG, platforms):
    self.platforms = platforms
    self.cfg = CFG
    log.debug("builder <C> initialized")

  def prepair(self, testInfo):
    TestName = testInfo.name()
    Platform = testInfo.platform()
    log.debug("<C> Builder prepair test <{}> in {}".format(TestName, testInfo.wd()))
    full_path = os.path.join(testInfo.wd(), TestName)
    log.debug("   test <{}> src: {}".format(TestName, testInfo.src()))
    log.debug("   test <{}> coping sources to: {}".format(TestName, full_path))
    copy_tree(testInfo.src(), full_path)
    # copy platform configuration files
    # create list of sources
    # render makefile
    test_binary = "test.elf"
    log.debug(self.cfg)
    KV = {
      "@platform_compiler" : "gcc",
      "@platform_cflags" : [],
      "@test_binary" : test_binary,
      "@src_files" : [],
      "@run_string" : ""
    }
    self.renderMakefile(testInfo.wd(), KV, "makefile_c.erb")
    return testInfo

