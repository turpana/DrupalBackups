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
  print "I RAN!"

