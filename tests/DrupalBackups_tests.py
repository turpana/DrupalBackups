from nose.tools import *
from DrupalBackups.drupalbackups import DrupalBackups
import pprint

def setup():
  print "SETUP!"

def teardown():
  print "TEAR DOWN!"

def test_configure():
  backups = DrupalBackups()
  configfilefound = backups.check_config()
  assert not configfilefound
  backups.configfile = "./tests/drupalservers.json"
  configfilefound = backups.check_config()
  assert configfilefound
  backups.config()
  pp = pprint.PrettyPrinter(indent=2)
  pp.pprint(backups.servers)
  print "I RAN!"

