===============
Getting Started
===============

This section describes how to organize this work and how to get the code running. Currently this assumes familiarity with Python projects, UNIX systems, and Git.

Getting Organized
-----------------

The running assumption is that `Data/` contains the .csv files representing the data set, and this `PHI/` repository contains the code and documentation.

Each may be stored as follows (though this may be tweaked through config files):

.. code-block:: bash

  Precision-Health-Initiative/
  ├── Data/
  │   ├── pregnancy_outcomes.csv
  │   ├── Screening.csv
  │   └── Visit1.csv
  └── PHI/
      └── README.md

Getting Running
---------------

Clone the repository from GitHub:

.. code-block:: bash

  git clone git@github.com:batflyer/PHI.git

If you're using Anaconda, this would be a good time to create an environment:

.. code-block:: bash

  conda create -n PHI python=3.6

… and install dependencies.

.. code-block:: bash

  pip install -r phi/requirements.txt
