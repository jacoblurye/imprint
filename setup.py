# -*- coding: utf-8 -*-
 
"""setup.py: setuptools control."""
 
import re
from setuptools import setup

version = re.search(
  '^__version__\s*=\s*"(.*)"',
  open('imprint/imprint.py').read(),
  re.M
  ).group(1)

descr = "Convert and display images and videos as string representations."
long_descr = descr

setup(
  name = "imprint",
  packages = ["imprint"],
  entry_points = {
      "console_scripts": ['imprint = imprint.__main__']
      },
  version = version,
  description = descr,
  long_description = long_descr,
  author = "Jacob Lurye",
  author_email = "jlurye96@gmail.com",
  url = "https://github.com/jacoblurye/imprint",
)