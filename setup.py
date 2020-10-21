from numpy.distutils.core import Extension
from numpy.distutils.core import setup

symmol = Extension(name='symmol', sources=['symmol.f90', 'symmol.pyf'])


setup(name='Symmetrize XYZ',
      description='Some helpers symmetrizing molecule geometries',
      author='Mirko Scholz',
      ext_modules=[symmol])

      

