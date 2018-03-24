#!/usr/bin/env python
#this is the standard way of installing a Python module, using distutils:
#sudo ./setup.py install
#uninstall is not provided, see https://stackoverflow.com/questions/1550226

from distutils.core import setup

setup(name='LiSpeak4',
      version='0.1',
      description='Linux Voice Command and Control System',
      author='Luca Vercelli, Brett Mayson et al.',
      author_email='luca.vercelli.to@gmail.com',
      url=None,
      packages=['lispeak'],
      scripts=['scripts/lispeak'],
      license='GPL-3.0'
     )
