from nose.tools import *
from DrupalBackups.drupalbackups import DrupalBackups
from os import path

def setup():
  print "SETUP!"

def teardown():
  print "TEAR DOWN!"

def test_configure():
  backups = DrupalBackups()
  assert not backups.self_config()
  backups.configfile = "./tests/drupalservers.json"
  assert backups.self_config()
  assert 'www.example.com' == backups.servers[0]['name']
  print "I RAN!"

def test_backup_all_now():
  backups = DrupalBackups()
  backups.configfile = "./tests/drupalservers.json"
  assert backups.self_config()
  assert backups.backup_all_now()

def test_create_archive():
  backups = DrupalBackups()
  backups.configfile = "./tests/drupalservers.json"
  assert backups.self_config()
  test_info = backups.create_archive(backups.servers[0])
  assert test_info['gathered']
  assert path.isfile(test_info['filepath'])

def test_backup_ard():
  backups = DrupalBackups()
  backups.configfile = "./tests/drupalservers.json"
  assert backups.self_config()
  assert backups.backup_ard(backups.servers[0], backups.create_archive(backups.servers[0]))
