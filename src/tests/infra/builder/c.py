class Builder_C():
  def __init__(self, CFG, platforms):
    self.platforms = platforms
    self.cfg = CFG
    print("Builder: C")

  def prepair(self, testInfo):
    print("C Builder prepair: {} {}".format(testInfo.name(), testInfo.wd()))
    return testInfo

