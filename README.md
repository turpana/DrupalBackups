Simple Drupal Backups
==============

**This is a work in progress.** My goal is to make a simple utility to help me automate all my drupal backups. Also, I'm learning python, git, and github.

### Intended usage

* create a directory where you want to keep your backups
* place drupalbackups.py and fabfile.py in this folder
* place a json configuration in the directory (see tests folder for example configuration)
* make sure drush is setup on each drupal server
* then:

        $ python drupalbackups.py

