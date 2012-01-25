Drupal Backups
==============

**This is a work in progress.** My goal is to make a simple utility to help me automate all my drupal backups. Also, I'm learning python, git, and github.

### Expected usage

* place a json configuration in the directory where the backups will be stored
* then run in  a python script:

        backups = DrupalBackups()
        backups.backup_all_now()
