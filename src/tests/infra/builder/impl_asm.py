import logging as log
from .basic_builder import BasicBuilder

class Builder_ASM(BasicBuilder):
  def __init__(self, CFG, platforms):
    self.platforms = platforms
    self.cfg = CFG
    log.debug("builder <ASM> initialized")

  def prepair(self, testInfo):
    log.debug("<ASM> Builder prepair test <{}>".format(testInfo.name()))
    return testInfo

