try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'Ayush'
}

setup(**config)
