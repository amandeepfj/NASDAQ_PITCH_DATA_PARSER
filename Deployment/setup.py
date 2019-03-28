import pyximport
pyximport.install(setup_args={"script_args":["--compiler=mingw32"]}, reload_support=True)

import setuptools
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('vwap.pyx'))