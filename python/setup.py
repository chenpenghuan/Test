from distutils.core import setup
from Cython.Build import cythonize
setup(name='server',
      ext_modules=cythonize("server.py"))
