#!/usr/bin/env python

from setuptools import setup, find_packages
from jubatest.version import get_version

setup(
    name             = 'jubatest',
    version          = get_version(),
    description      = 'A test tool for distributed enviropment.',
    author           = 'IMAMASU Ryohei',
    author_email     = 'imms.ryohei@gmail.com',
    packages         = find_packages(),
    install_requires = [
        'pyyaml',
        'fabric',
    ],
    entry_points     = {
        'console_scripts': [
            'jubatest = jubatest.main:main',
        ]
    },
)
