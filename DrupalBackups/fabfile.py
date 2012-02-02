from __future__ import with_statement
from fabric.api import run, cd
def ard(drupal_dir, drush_command):
  drupal_dir = drupal_dir.strip('\'')
  drush_command = drush_command.strip('\'')
  with cd(drupal_dir):
    run(drush_command)

