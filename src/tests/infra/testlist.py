import logging as log
from pathlib import Path

import yaml
import os

class TestItem():
  def __init__(self, name, platform, builder, header, attrs, pwd, src_root):
    self._name = name
    self._platform = platform
    self._builder = builder
    self._pwd = pwd
    self._attrs = attrs
    self._fallback = header
    self._src_root = src_root

  def name(self):
    return "{}_{}_{}".format(self._builder.name, self._platform, self._name)

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

def extractPlatforms(header, body, bldr):
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

  def tests(self):
    return self._list

  def __init__(self, builder, the_list, subdir, output):

    self._builder = builder
    self._list = []
    self._source = the_list

    SRC_ROOT = str(Path(the_list).parent.absolute())
    log.info("Testlist file: {}".format(the_list))

    self._outdir = os.path.join(output, subdir)
    log.debug("    OutDir: {}".format(self._outdir))


    # Here we have a race condition - but I don't bother
    if not os.path.exists(self._outdir):
      os.makedirs(self._outdir)

    # TODO: consider creating another directory named after the testlist file
    log.debug("   FullDir: {}".format(self._outdir))

    with open(str(the_list), 'r') as stream:
      header, body = yaml.safe_load_all(stream)
      log.debug(header, body)
      for name, args in body.items():
        platforms = extractPlatforms(header, args, builder)
        for platform in platforms:
          test_description = TestItem(name, platform, builder,
                                      header, args, self._outdir, SRC_ROOT)
          #test = builder.prepair(test_description)
          self._list.append(test_description)
    log.info("    testlist has {} items".format(len(self._list)))

