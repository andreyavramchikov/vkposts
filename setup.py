# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import vkposts
version = vkposts.__version__

setup(
    name='vkposts',
    version=version,
    author='Andrey',
    author_email='aldrson@gmail.com',
    packages=[
        'vkposts',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['vkposts/manage.py'],
)
