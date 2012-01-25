from nose.tools import *
from DrupalBackups.drupalbackups import DrupalBackups

def setup():
  print "SETUP!"

def teardown():
  print "TEAR DOWN!"

def test_configure():
  backups = DrupalBackups()
  configfilefound = backups.self_config()
  assert not configfilefound
  backups.configfile = "./tests/drupalservers.json"
  configfilefound = backups.self_config()
  assert configfilefound
  print "I RAN!"

