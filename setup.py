#!/usr/bin/env python3
'''
Created on Apr. 26, 2019

@author: jldupont
'''
__author__ = "Jean-Lou Dupont"
__version__ = "0.1"

DESC="""
Feature Collection geojson file to NL JSON of geometry objects
"""

from distutils.core import setup
from setuptools import find_packages


setup(name=         'jldgeo',
      version=      __version__,
      description=  'Geojson converter',
      author=       __author__,
      author_email= 'jl@jldupont.com',
      url=          'https://github.com/jldupont/jldgeo',
      package_dir=  {'': "src",},
      packages=     find_packages("src"),
      scripts=      ['src/scripts/jldgeo'
                     ],
      zip_safe=False
      ,long_description=DESC
      ,install_requires=[ "click>=7.0" 
                         ,'ijson>=2.3'
                         ]
      )

#############################################

f=open("latest", "w")
f.write(str(__version__)+"\n")
f.close()