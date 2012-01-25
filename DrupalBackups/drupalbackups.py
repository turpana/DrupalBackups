# -*- coding:utf-8 -*-
import fileinput
import os
import pprint
from time import strftime, gmtime
try:
  import jsonlib2 as json
except ImportError:
  import json

class DrupalBackups(object):
  configfile = './drupalservers.json'

  def __init__(self):
    self.self_config()

  def self_config(self):
    if (not os.path.isfile(self.configfile)):
      print 'Warning: config file "drupalservers.json" not found.\n'
      return False
    self.config()
    return True

  def config(self):
    json_data = open(self.configfile)
    data = json.load(json_data)
    self.servers = data['servers']
    json_data.close()
    self.backups_dir = os.getcwd()
    return True

  def backup_all_now(self):
    print 'Backing up all sites now to ' + self.backups_dir + '/'
    for s in self.servers:
      print 'Backing up '+ s['name']
      if (not os.path.exists(self.backups_dir + '/' + s['name'])):
        try:
          os.mkdir(self.backups_dir + '/' + s['name'])
        except OSError:
          print "Error adding directory for "+s['name']+", please ensure you have write privileges"
          break
      timestamp = strftime('%Y-%m-%d-%H%M', gmtime())
      timestamped_dirname = '/'.join([self.backups_dir, s['name'], timestamp]) + '/'
      print timestamped_dirname 

    print 'Not implemented, so returning False'
    return False
