# nuMoM2b Preprocessing — Precision Health Initiative (φ)

A module for creating reproducible partitions of the nuMoM2b data set based on configuration files.

[![Documentation Status](https://readthedocs.org/projects/numom2b-preprocessing/badge/?version=latest)](https://doc.numom2b.org/en/latest/?badge=latest)
[![LGTM Code Review](https://img.shields.io/lgtm/grade/python/github/hayesall/nuMoM2b_preprocessing?label=code%20quality&logo=lgtm)](https://lgtm.com/projects/g/hayesall/nuMoM2b_preprocessing/context:python)
[![Build Status](https://travis-ci.com/hayesall/nuMoM2b_preprocessing.svg?branch=master)](https://travis-ci.com/hayesall/nuMoM2b_preprocessing)
[![codecov](https://codecov.io/gh/hayesall/nuMoM2b_preprocessing/branch/master/graph/badge.svg)](https://codecov.io/gh/hayesall/nuMoM2b_preprocessing)

* Maintained by [Alexander L. Hayes](https://hayesall.com)
* Documentation on https://doc.numom2b.org/en/latest/

## Getting Started

**Data should not be stored here.**

Familiarity with Python, UNIX systems, and Git would be helpful.

### Getting Organized

The running assumption is that `Data/` contains the .csv files representing
the data set, and this `nuMoM2b_preprocessing/` repository contains the code
and documentation.

Each might be stored as follows (though this may be tweaked through config files):

```
Precision-Health-Initiative/
├── Data/
│   ├── pregnancy_outcomes.csv
│   ├── Screening.csv
│   └── Visit1.csv
└── nuMoM2b_preprocessing/
    └── README.md
```

### Getting Running

Clone the repository from GitHub:

```bash
git clone git@github.com:hayesall/nuMoM2b_preprocessing.git
```

If you're using Anaconda, this would be a good time to create an environment:

```bash
conda create -n PHI python=3.7
```

... and install dependencies.

```bash
pip install -r phi/requirements.txt
```

## Using `nuMoM2b_preprocessing`

* ### As a Package

  Installing using the setup script adds a `numom2b_preprocessing` package.

  ```bash
  python setup.py install
  ```

  ... which can then be imported

  ```python
  import numom2b_preprocessing

  _params = numom2b_preprocessing.parameters(config="phi_config.json")
  numom2b_preprocessing.run(_params)
  ```

* ### As a Commandline (CLI) Tool

  Installing using `setup.py` adds an entry point to your default `bin/` directory.

  ```bash
  python setup.py install
  ```

  This adds a `numom2b_preprocessing` tool which can be invoked as follows:

  ```bash
  numom2b_preprocessing --help
  ```

* ### As a Submodule

  `nuMoM2b_preprocessing` acts as the first step in building classification
  pipelines. To incorporate it in later learning steps, it may be useful to
  have access to the methods as a submodule. For general documentation on using
  submodules, refer to the
  [Git Manual](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

  ```bash
  git submodule add git@github.com:hayesall/nuMoM2b_preprocessing.git
  ```

  The modules in the package can then be accessed as normal.

  ```python
  import nuMoM2b_preprocessing.numom2b_preprocessing

  _params = numom2b_preprocessing.parameters(config="phi_config.json")
  numom2b_preprocessing.run(_params)
  ```

## [nuMoM2b_preprocessing Documentation](https://doc.numom2b.org/en/latest/)

Documentation is not currently hosted at https://doc.numom2b.org/en/latest/,
but local copies may be built using
[Sphinx](http://www.sphinx-doc.org/en/master/).

A separate requirements file is in the `documentation/` directory.

```bash
pip install -r documentation/requirements.txt
```

A `make.bat` and `Makefile` are included:

```bash
cd documentation
make html
```

If the build is successful, a copy will reside in a new `build/html/` directory.

```bash
open build/html/index.html          # (macOS)
xdg-open build/html/index.html      # (Linux — "should" open with default browser)
```
