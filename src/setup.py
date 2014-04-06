#!/usr/bin/env python3
from cx_Freeze import setup, Executable
import bullshit

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['os', 'argparse', 'time', 'sys'], excludes = [])

base = 'Console'

executables = [
    Executable('bullshit.py', base=base, targetName = 'bullshit.exe')
]

setup(name='The Bullshit Performance Standard',
      version = bullshit.version,
      description = 'Easily benchmark your computer using bullshit!',
      options = dict(build_exe = buildOptions),
      executables = executables)
