from nose.tools import *
from DrupalBackups.drupalbackups import DrupalBackups

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

def test_gather_site_info():
  backups = DrupalBackups()
  backups.configfile = "./tests/drupalservers.json"
  assert backups.self_config()
  test_info = backups.gather_site_info(backups.servers[0])
  assert 'sites/default/files' == test_info['file_public_path']
  assert '~/Documents/Sites/www.example.com/private_files' == test_info['file_private_path']
