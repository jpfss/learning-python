#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:01:37 2023

@author: jpfss
"""

from distutils.core import setup, Extension
module1 = Extension('Test', sources=['add.c'])
setup(name='Test',
      version='1.0',
      description='This is a demo package',
      ext_modules=[module1])
