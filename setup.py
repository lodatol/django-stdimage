# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='django-stdimage',
    version='0.2.2',
    description='Django Standarized Image Field',
    author='Garcia Marc, Steven Klass',
    author_email='garcia.marc@gmail.com, sklass@pivotalenergysolutions.com',
    url='https://github.com/pivotal-energy-solutions/django-stdimage',
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
