from nose.tools import *
from DrupalBackups.drupalbackups import DrupalBackups

def setup():
  print "SETUP!"

def teardown():
  print "TEAR DOWN!"

def test_configure():
  backups = DrupalBackups()
  configfilefound = backups.config()
  assert configfilefound
  print "I RAN!"

