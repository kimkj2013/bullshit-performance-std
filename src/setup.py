from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["os", "argparse", "time"], excludes = [])

base = 'Console'

executables = [
    Executable('bullshit.py', base=base, targetName = 'bullshit.exe')
]

setup(name='The Bullshit Performance Standard',
      version = '0.5.0',
      description = 'Easily benchmark your computer using bullshit!',
      options = dict(build_exe = buildOptions),
      executables = executables)
