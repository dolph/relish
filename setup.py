#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='relish',
    version='1.0',
    description='Serialize your python objects into tasty (human-readable) formats.',
    author='Dolph Mathews',
    author_email='dolph.mathews@gmail.com',
    url='http://github.com/dolph/relish/',
    packages=['relish'])
