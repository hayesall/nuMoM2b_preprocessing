===============
Getting Started
===============

This section describes how to get organized and get the code running. This will try to keep concepts
as accessible as possible, but some familiarity with Python projects, UNIX systems, and Git would
certainly be helpful.

Getting Organized
-----------------

The running assumption will be that the nuMoM2b data is contained in a directory (likely unzipped from a
``numom2b.zip``), and this ``nuMoM2b_preprocessing/`` repository is available on your local machine.

For example, we find it helpful to organize work as follows (though these may be tweaked with config files):

.. code-block:: text

  Precision-Health-Initiative/
  ├── Data/
  │   ├── pregnancy_outcomes.csv
  │   ├── Screening.csv
  │   └── Visit1.csv
  └── nuMoM2b_preprocessing/
      ├── README.md
      └── phi/

``nuMoM2b_preprocessing`` may be cloned from GitHub:

.. code-block:: bash

    git clone https://github.com/batflyer/nuMoM2b_preprocessing.git

If you're using `Anaconda <https://www.anaconda.com/distribution/>`_, this would be a good time to create an environment:

.. code-block:: bash

    conda create -n PHI python=3.7
    conda activate PHI

… and install dependencies.

.. code-block:: bash

  pip install -r phi/requirements.txt

Documentation
-------------

Documentation is currently hosted at https://doc.nuMoM2b.org, but local copies may also be built using
`Sphinx <http://www.sphinx-doc.org/en/master/>`_.

A separate requirements file is in the ``documentation/`` directory.

.. code-block:: bash

    pip install -r documentation/requirements.txt

A ``make.bat`` and ``Makefile`` are included:

.. code-block:: bash

    cd documentation
    make html

If the build is successful, a copy will reside in a new ``build/html/`` directory.

.. code-block:: bash

    open build/html/index.html          # (macOS)
    xdg-open build/html/index.html      # (Linux)
