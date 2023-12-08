#! /usr/bin/env python

"""
setup.py of the Modbus_test module
"""
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages = ['Modbus_test'],
    package_dir = {'': 'src'}
)
setup(**d)