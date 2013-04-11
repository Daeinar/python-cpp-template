# -*- encoding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourcefiles = ['interface.pyx']
ext_modules = [Extension("testlib", sourcefiles, language="c++", extra_compile_args=["-O3","-march=native"])]

setup(
  name = 'testlib app',
  cmdclass = {'build_ext': build_ext}, 
  ext_modules = ext_modules
)
