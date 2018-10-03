#!/usr/bin/env python
"""setup file for nanochat"""
from setuptools import (
    setup,
    find_packages
)
from nanochat.globals import (
    __version__
)


PROJECT = 'nanochat'
VERSION = __version__
setup(
    name=PROJECT,
    version=VERSION,
    description='',
    long_description='',
    author='Vinesh Kannan',
    author_email='vinesh@mimirhq.com',
    url='',
    py_modules=[PROJECT],
    download_url='',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],
    platforms=['Any'],
    scripts=[],
    provides=[],
    install_requires=[],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points={}
)
