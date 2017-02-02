from cx_Freeze import setup, Executable

import os

os.environ['TCL_LIBRARY'] = "C:\\Python3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Python3\\tcl\\tk8.6"

# Dependencies are automatically detected, but it might need
# fine tuning.
include_files = [r"C:\Python3\DLLs\tcl86t.dll", \
                 r"C:\Python3\DLLs\tk86t.dll"] 
buildOptions = dict(packages = [], excludes = [], include_files=include_files)

base = 'Console'

executables = [
    Executable('Calculatrice.pyw', base=base)
]

setup(name='Calculatrice',
      version = '1.0',
      description = 'Une simple Calculatrice',
      options = dict(build_exe = buildOptions),
      executables = executables)
