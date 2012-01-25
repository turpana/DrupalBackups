Drupal Backups
==============

**This is a work in progress.** My goal is to make a simple utility to help me automate all my drupal backups. Also, I'm learning python, git, and github.

### Expected usage

* create a json configuration file describing each site's info
* then:

        backups = DrupalBackups()
        backups.backup_all_now()
