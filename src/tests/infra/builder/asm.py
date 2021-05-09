class Builder_ASM():
  def __init__(self, CFG, platforms):
    self.platforms = platforms
    self.cfg = CFG
    print("Builder: ASM")

  def prepair(self, testInfo):
    print("ASM Builder prepair: {}".format(testInfo.name))
    return testInfo

