# -*- coding:utf-8 -*-
import fileinput
from os import path
import pprint
try:
  import jsonlib2 as json
except ImportError:
  import json

class DrupalBackups(object):
  configfile = './drupalservers.json'

  def __init__(self):
    self.self_config()

  def self_config(self):
    if (not path.isfile(self.configfile)):
      print 'Warning: config file "drupalservers.json" not found.\n'
      return False
    self.config()
    return True

  def config(self):
    json_data = open(self.configfile)
    data = json.load(json_data)
    self.servers = data['servers']
    json_data.close()
    return True

  def backup_all_now(self):
    print 'Backing up servers'
