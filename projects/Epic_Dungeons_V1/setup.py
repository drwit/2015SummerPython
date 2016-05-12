try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Epic Dungeons',
	'author': 'WU',
	'url': ' ',
	'download_url': ' ',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Epic Dungeons'
}

setup(**config)