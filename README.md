Drupal Backups
==============
This is a work in progress. My goal is to make a simple utility to help me automate all my drupal backups. Also, I'm learning python and git.

### Expected usage
1. create a json configuration file describing each site's info
2. then:

'''python
backups = DrupalBackups()
backups.backup_all_now()
'''


