#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(gluque): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='qiime_2_ll_quick_viewer',
    version='0.2.5',
    description="Ley Lab Quick Viewer for Qiime 2 artifacts.",
    long_description=readme + '\n\n' + history,
    author="Guillermo Luque",
    author_email='guillermo.luque.ds@gmail.com',
    url='https://github.com/leylabmpi/qiime_2_ll_quick_viewer',
    packages=find_packages(include=['qiime_2_ll_quick_viewer']),
    entry_points={
        'console_scripts': [
            'qiime_2_ll_quick_viewer=qiime_2_ll_quick_viewer.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='qiime_2_ll_quick_viewer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
