#!/usr/bin/env python

from distutils.core import setup
 
long_description = open('README').read()
 
setup(
    name='untappd',
    version="0.1",
    py_modules = ['untappd'],
    description='A python library for the Untappd.com API',
    author='Xavier Santolaria',
    author_email='xavier@santolaria.net',
    license='BSD License',
    url='http://github.com/xsa/pyuntappd/',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
