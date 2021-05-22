import logging as log
from pathlib import Path

import yaml
import os

class TestItem():
  def __init__(self, name, platform, body, header, pwd, src_root):
    self._name = name
    self._platform = platform
    self._pwd = pwd
    self._attrs = body
    self._fallback = header
    self._src_root = src_root

  def name(self):
    return "{}_{}".format(self._platform, self._name)

  def wd(self):
    return os.path.join(self._pwd, self.name())

  def platform(self):
    return self._platform

  def labels(self):
    return self._getProperty('labels', [])

  def src(self):
    return os.path.join(self._src_root, self._getProperty('src'))

  def _getProperty(self, prop, default = None):
    if prop in self._attrs:
      return self._attrs[prop]
    if prop in self._fallback:
      return self._fallback[prop]

    if default != None:
      return default

    raise "could not find property {}".format(prop)

def extractPlatforms(header, body):
  platforms = None
  if 'platforms' in body:
    platforms = body['platforms']
  elif 'platforms' in header:
    platforms = header['platforms']
  if platforms == None:
    log.error("could not extract platforms for {}/{}".format(body, header))
    raise ValueError("could not extract platforms from test description")
  if isinstance(platforms, str):
    platforms = [p.strip() for p in platforms.split(',')]
  if not isinstance(platforms, list):
    log.error("n/a platform format:")
    log.error(platforms)
    raise ValueError("could not derive platforms for test")
  return platforms


class TestList():
  def __init__(self, builder, the_list, subdir, output):
    self.list = []
    SRC_ROOT = str(Path(the_list).parent.absolute())
    log.info("Testlist: {}".format(the_list))
    log.debug("    OutDir: {}".format(output))
    Dir = os.path.join(output, subdir)

    # Here we have a race condition - but I don't bother
    if not os.path.exists(Dir):
      os.makedirs(Dir)

    # TODO: consider creating another directory named after the testlist file
    log.debug("   FullDir: {}".format(Dir))

    with open(str(the_list), 'r') as stream:
      header, body = yaml.safe_load_all(stream)
      log.debug(header, body)
      for name, args in body.items():
        platforms = extractPlatforms(header, args)
        for platform in platforms:
          test_description = TestItem(name, platform, body, args, Dir, SRC_ROOT)
          test = builder.prepair(test_description)
          self.list.append(test)
    log.info("    testlist has {} items".format(len(self.list)))

