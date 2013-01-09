# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='django-stdimage',
    version='0.2.1',
    description='Django Standarized Image Field',
    author='garcia.marc',
    author_email='garcia.marc@gmail.com',
    url='http://code.google.com/p/django-stdimage/',
    license='Apache License (2.0)',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={'stdimage': ['static/js/*.js', 'templates/stdimage/*.html']},
    include_package_data=True,
)
