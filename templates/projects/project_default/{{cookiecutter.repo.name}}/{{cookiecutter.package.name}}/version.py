import sys

# format: ('_major', '_minor', '_patch')
__version__ = "{{ cookiecutter.module.version }}"
__author__  = "{{ cookiecutter.author.full_name }}"
watermark   = dict(python=f"{sys.version_info.major}.{sys.version_info.minor}")
