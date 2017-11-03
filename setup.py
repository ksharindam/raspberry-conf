#!/usr/bin/env python

from setuptools import setup
from raspi_conf import version

setup(
      name='raspi-conf',
      version=__version__,
      description='Graphical Configuration manager for Raspberry Pi 2',
      keywords='raspberry pi configuration',
      url='http://github.com/ksharindam/raspberry-conf',
      author='Arindam Chaudhuri',
      author_email='ksharindam@gmail.com',
      license='GPLv3',
      packages=['raspi_conf'],
#      install_requires=['PyQt4',      ],
      entry_points={
          'console_scripts': ['raspi-conf=raspi_conf.main:main'],
      },
#      include_package_data=True,
      zip_safe=False)
