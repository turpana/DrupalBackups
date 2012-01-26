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
    errors = 0
    for s in self.servers:
      print 'Backing up '+ s['name']
      if (not os.path.exists(self.backups_dir + '/' + s['name'])):
        try:
          os.mkdir(self.backups_dir + '/' + s['name'])
        except OSError:
          print "Error adding directory for "+s['name']+", please ensure you have write privileges."
          break
      ard = self.create_archive(s)
      if not ard['gathered']:
        print "Error creating backup for "+s['name']
        break
      errors += self.backup_ard(s, ard)
    return True

  def create_archive(self, s):
    if s['location'] != 'local':
      return {'gathered': False}
    ard = {}
    cwd = os.getcwd()
    os.chdir(s['root_dir'])
    popen = subprocess.Popen([s['drush'], "ard", "--pipe"], stdout=subprocess.PIPE)
    output = popen.communicate()
    ard['filepath'] = output[0].strip()
    ard['gathered'] = True
    os.chdir(cwd)
    return ard

  def backup_ard(self, s, ard):
    if s['location'] != 'local':
      return False
    print '*****'
    print ' '+s['name']
    cwd = os.getcwd()
    os.chdir(s['name'])
    source_dir = ard['filepath']
    print 'Copying from: '+ source_dir + ' to: ' + './' 
    popen = subprocess.Popen(["cp", source_dir, './'], stdout=subprocess.PIPE)
    os.chdir(cwd)
    print '*****'
    return True
