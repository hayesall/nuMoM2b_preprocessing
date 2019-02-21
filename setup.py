# Copyright 2019 Alexander L. Hayes

from setuptools import setup
from setuptools import find_packages

setup(
    name='phi',
    version='0.0.1',
    packages=find_packages(exclude=["unittests"]),
    url='https://github.com/batflyer/PHI',
    license='Not-Declared',
    author='Alexander L. Hayes (@batflyer)',
    author_email='alexander@batflyer.net',
    description='Python API for experimenting with Precision Health Data',
    entry_points={
    'console_scripts': ['phi=phi.__main__']
    },
)
