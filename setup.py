#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

readme = open('README.md').read()

setup(
    name='git-lint-diff',
    version='0.1.0',
    description='A tool to limit what lines of files checked so that you can gradually reach a lint free repository',
    long_description=readme,
    author='Simon Yu',
    author_email='xm.yuau@gmail.com',
    url='https://github.com/monash-merc/git-lint-diff',
    packages=find_packages(exclude=['tests', 'local']),
    include_package_data=True,
    install_requires=[],
    license="GPLv3+",
    zip_safe=False,
    keywords='monash-merc/git-lint-diff',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
)
