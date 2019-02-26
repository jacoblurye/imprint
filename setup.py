# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*\'(.*)\'',
    open('imprint/imprint.py').read(),
    re.M
).group(1)

install_requires = [
    'numpy>=1.14.3',
    'scikit-image>=0.13.1',
    'scikit-video>=1.1.10'
]

descr = 'Convert and display images and videos as string representations.'
long_descr = descr

setup(
    name='imprint',
    packages=['imprint'],
    version=version,
    entry_points={
        'console_scripts': ['imprint = imprint.cli:main']
    },
    install_requires=install_requires,
    description=descr,
    long_description=long_descr,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    author='Jacob Lurye',
    author_email='jlurye96@gmail.com',
    url='https://github.com/jacoblurye/imprint'
)
