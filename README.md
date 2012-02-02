Simple Drupal Backups
==============

My goal is to make a simple utility to help me automate all my drupal backups.

### Usage

In a directory you want to keep your backups:

* place drupalbackups.py and fabfile.py
* place a json configuration in the directory (see tests folder for example configuration)
* then:

        $ python drupalbackups.py


### Requires 

* fabric
* drush on each server
