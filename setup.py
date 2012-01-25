try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
    'description': 'Drupal backup script for multiple websites',
    'author': 'Turpana Molina',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'develop@turpana.com',
    'versions': '0.1',
    'install_requires': ['nose'],
    'packages': ['DrupalBackups'],
    'scripts': [],
    'name': 'drupalbackups'
}

setup(**config)
