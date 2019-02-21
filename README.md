# nuMoM2b Preprocessing — Precision Health Initiative (φ)

A module for creating reproducible partitions of the nuMoM2b data set based on configuration files.

## Getting Started

Data should not be stored here.

This section describes how to organize this work and how to get the code running. Currently this assumes familiarity with Python projects, UNIX systems, and Git.

#### Getting Organized

The running assumption is that `Data/` contains the .csv files representing the data set, and this `PHI/` repository contains the code and documentation.

Each may be stored as follows (though this may be tweaked through config files):

```bash
Precision-Health-Initiative/
├── Data/
│   ├── pregnancy_outcomes.csv
│   ├── Screening.csv
│   └── Visit1.csv
└── nuMoM2b_preprocessing/
    └── README.md
```

#### Getting Running

Clone the repository from GitHub:

```bash
git clone git@github.com:batflyer/nuMoM2b_preprocessing.git
```

If you're using Anaconda, this would be a good time to create an environment:

```bash
conda create -n PHI python=3.6
```

... and install dependencies.

```bash
pip install -r phi/requirements.txt
```

## Using `nuMoM2b_preprocessing`

* #### As a Package

  Installing using the setup script adds a `phi` package.

  ```bash
  python setup.py install
  ```

  ... which can then be imported

  ```python
  from phi import get_config
  from phi import preprocess

  _params = get_config.parameters(config="phi_config.json")
  ```

* #### As a Commandline (CLI) Tool

  Installing using `setup.py` adds an entry point to your default `bin/` directory.

  ```bash
  python setup.py install
  ```

  This adds a `phi` tool which can be invoked as follows:

  ```
  $ phi --help
  usage: phi [-h] [-c CONFIG] [-l LOGGING] [-t] [-r]

  optional arguments:
    -h, --help            show this help message and exit
    -c CONFIG, --config CONFIG
                          Set the configuration file to read from
                          [Default:phi_config.json].
    -l LOGGING, --logging LOGGING
                          Set the verbosity of the Python logger [Default:10].
                          Follows Logging Levels.
    -t, --test            Display information for unit tests, code coverage, and
                          formatting.
    -r, --run             Run the pipeline (require explicit interaction
                          currently to help prevent accidents).
  ```

* #### As a Submodule

  `nuMoM2b_preprocessing` acts as the first step in building classification pipelines. To incorporate it in later learning steps, it may be useful to have access to the methods as a submodule. For general documentation on using submodules, refer to the [Git Manual](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

  ```bash
  git submodule add git@github.com:batflyer/nuMoM2b_preprocessing.git
  ```

  The modules in the package can then be accessed as normal.

  ```python
  from nuMoM2b_preprocessing.phi import get_config
  from nuMoM2b_preprocessing.phi import preprocess

  _params = get_config.parameters(config="phi_config.json")
  ```

## Documentation

Documentation is not currently hosted externally, but local copies may be built using [Sphinx](http://www.sphinx-doc.org/en/master/).

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
