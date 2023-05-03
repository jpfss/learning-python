#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:01:37 2023

@author: jpfss
"""

from distutils.core import setup, Extension

hello_module = Extension('hello', sources=['hello.c'])

setup(name='hello',

      version='0.1.0',

      description='Hello world module written in C',

      ext_modules=[hello_module])
