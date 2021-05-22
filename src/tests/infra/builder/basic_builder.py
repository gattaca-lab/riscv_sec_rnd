import subprocess
import os
from pathlib import Path
import logging as log

class BasicBuilder:
  def __init__(self, CFG,  platforms):
    self.cfg = CFG
    self.platforms = platforms

  def platforms():
    return self.platforms

  def config():
    return self.cfg

  def name(self):
    return self.name

  def renderRubyScript(self, RubyScript, KV, TemplatePath):
    with open(RubyScript, 'w') as f:
      for k in KV:
        v = KV[k]
        if isinstance(v, list):
          f.write("{} = [{}]\n".format(k, ",\n  ".join(KV[k])))
        else:
          f.write("{} = \"{}\"\n".format(k, KV[k]))
      f.write("\n")
      f.write("require 'erb'\n\n")
      f.write("TemplateString = File.read(\"{}\")\n".format(TemplatePath))
      f.write("print ERB.new(TemplateString).result(binding)\n")

  def renderMakefile(self, wd, KV, templateName):
    TemplatePath = os.path.join(str(Path(__file__).parent.absolute()), "templates")
    TemplatePath = os.path.join(TemplatePath, templateName)
    RubyScript = os.path.join(wd, 'renderMakefile.rb')

    log.debug("creating ruby script to render makefile: {}".format(RubyScript))
    self.renderRubyScript(RubyScript, KV, TemplatePath)

    MakeFile = os.path.join(wd, 'Makefile')
    with open(MakeFile, 'w') as mkf:
      subprocess.check_call(["ruby", RubyScript], cwd=wd, stdout = mkf)
