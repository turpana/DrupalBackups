# -*- coding:utf-8 -*-
import fileinput
import os
import pprint
from time import strftime, gmtime
import subprocess
import re
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
          print "Error adding directory for "+s['name']+", please ensure you have write privileges."
          break
      timestamp = strftime('%Y_%m_%d_%H%M_%S', gmtime())
      target_dir = '/'.join([self.backups_dir, s['name'], timestamp]) + '/'
      os.mkdir(target_dir)
      site_info = self.gather_site_info(s)
      if not site_info['gathered']:
        print "Error gathering site information for "+s['name']+". backup not completed."
        break

    print 'Not implemented, so returning False'
    return False

  def gather_site_info(self, s):
    if s['location'] != 'local':
      return {'gathered': False}
    vars = ['file_private_path', 'file_public_path']
    info = {}
    cwd = os.getcwd()
    os.chdir(s['root_dir'])
    for v in vars:
      popen = subprocess.Popen([s['drush'], "vget", v], stdout=subprocess.PIPE)
      output = popen.communicate()
      splitoutput = output[0].split('"')
      info[v] = splitoutput[1]
    info['gathered'] = True
    os.chdir(cwd)
    return info
