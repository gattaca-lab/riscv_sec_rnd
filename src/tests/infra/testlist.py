import yaml
import os

class TestItem():
  def __init__(self, name, body, header, pwd):
    self._name = name
    self._pwd = pwd
    self._attrs = body
    self._fallback = header

  def name(self):
    return self._name

  def wd(self):
    return self._pwd

  def platforms(self):
    return self._getProperty('platform')

  def labels(self):
    return self._getProperty('labels', [])

  def src(self):
    return self._getProperty('src')

  def _getProperty(self, prop, default = None):
    if prop in self._attrs:
      return self._attrs[prop]
    if prop in self._fallback:
      return self._fallback[prop]

    if default != None:
      return default

    raise "could not find property {}".format(prop)

class TestList():
  def __init__(self, builder, the_list, subdir, output):
    self.list = []
    print("Testlist: {}".format(the_list))
    print("OutDir: {}".format(output))
    Dir = os.path.join(output, subdir)

    # Here we have a race condition - but I don't bother
    if not os.path.exists(Dir):
      os.makedirs(Dir)

    # TODO: consider creating another directory named after the testlist file
    print("FullDir: {}".format(Dir))

    with open(str(the_list), 'r') as stream:
      header, body = yaml.safe_load_all(stream)
      print(header, body)
      for name, args in body.items():
        test_description = TestItem(name, body, args, Dir)
        test = builder.prepair(test_description)
        self.list.append(test)

