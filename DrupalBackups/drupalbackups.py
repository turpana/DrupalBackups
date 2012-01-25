# -*- coding:utf-8 -*-
import fileinput
from os import path
try:
  import jsonlib2 as json
except ImportError:
  import json

class DrupalBackups(object):
  configfile = 'drupalservers.json'

  def __init__(self):
    self.check_config()

  def check_config(self):
    if (not path.exists(self.configfile)):
      print 'Config file "drupalservers.json" not found.\n'
      return False
    return True

  def config(self):
    if (self.check_config()):
      json_data = open(self.configfile)

  def backup_all_now():
    print 'Backing up servers'
