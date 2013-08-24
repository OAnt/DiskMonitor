try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'Antoine Orozco',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'orozco_antoine@yahoo.fr'
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['__main__', 'DirectorySizeOrdering','GeneralFunctions'],
    'scripts': ['DMWebInterface'],
    'name': 'DiskMonitor'
}

setup(**config)

##
