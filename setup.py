# Copyright © 2019 Alexander L. Hayes

from setuptools import setup
from setuptools import find_packages
from os import path

# Get __version__ from _meta.py
with open(path.join("numom2b_preprocessing", "_meta.py")) as f:
    exec(f.read())

setup(
    name="numom2b_preprocessing",
    version=__version__,
    packages=find_packages(exclude=["unittests"]),
    url="https://github.com/hayesall/nuMoM2b_preprocessing",
    license="MIT",
    author="Alexander L. Hayes (@hayesall)",
    author_email="hayesall@iu.edu",
    description="Create reproducible partitions of the nuMoM2b data set based on configuration files.",
    entry_points={
        "console_scripts": ["numom2b_preprocessing=numom2b_preprocessing.__main__"]
    },
    install_requires=['numpy', 'pandas']
)
