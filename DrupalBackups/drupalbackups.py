# -*- coding:utf-8 -*-
from __future__ import with_statement
import fileinput
import os
import pprint
from time import strftime, gmtime
from fabric.api import local, run
import subprocess
import re
try:
  import jsonlib2 as json
except ImportError:
  import json

class DrupalBackups(object):
  configfile = './drupalservers.json'
  re_out = re.compile('.*out:')

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
    ard = {}
    if s['location'] == 'local':
      cwd = os.getcwd()
      os.chdir(s['drupal_root'])
      popen = subprocess.Popen([s['drush'], "ard", "--pipe"], stdout=subprocess.PIPE)
      output = popen.communicate()
      ard['filepath'] = output[0].strip()
      ard['gathered'] = True
      os.chdir(cwd)
      return ard
    if s['location'] == 'remote':
      popen = subprocess.Popen(['fab', '-H', '%s@%s' % (s['user'], s['host']), "ard:drupal_dir=%s,drush_command='%s --pipe ard'" % (s['drupal_root'], s['drush'])], stdout=subprocess.PIPE)
      output = popen.communicate()[0].split('\n')
      for o in output:
        try:
          if (self.re_out.search(o)):
              ard['filepath'] = self.re_out.sub('',o).strip()
              print 'filepath: %s' % ard['filepath']
              ard['gathered'] = True
              return ard
        except TypeError, e:
          break
      ard['gathered'] = False
      return ard

  def backup_ard(self, s, ard):
    if s['location'] == 'local':
      cwd = os.getcwd()
      os.chdir(s['name'])
      source = ard['filepath']
      print 'Copying '+ source + ' to: ' + cwd + '/' + s['name']
      popen = subprocess.Popen(["cp", source, './'], stdout=subprocess.PIPE)
      os.chdir(cwd)
      return True
    if s['location'] == 'remote':
      cwd = os.getcwd()
      os.chdir(s['name'])
      source = ard['filepath']
      for v in source.split('/'):
        target = v 
      print 'Copying' + source + ' to: ' + cwd + '/' + s['name']
      popen = subprocess.Popen(["scp", '%s@%s:%s' % ( s['user'], s['host'], source ), target], stdout=subprocess.PIPE)
      os.chdir(cwd)
      return True

if __name__ == '__main__':
  backups = DrupalBackups()
  backups.backup_all_now()
