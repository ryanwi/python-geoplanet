from setuptools import setup, find_packages
import sys, os

version = '0.1'

install_requires = [
    # -*- Extra requirements: -*-
    ]

def _py26OrGreater():
    return sys.hexversion > 0x20600f0

if not _py26OrGreater():
    install_requires.append("simplejson>=1.7.1")


setup(name='python-geoplanet',
      version=version,
      description="An API for GeoPlanet (http://developer.yahoo.com/geo/geoplanet/)",
      long_description=open("./README", "r").read(),
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Development Status :: ",
          "Environment :: ",
          "Intended Audience :: ",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='geoplanet, geo',
      author='',
      author_email='',
      url='',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      """,
      )
