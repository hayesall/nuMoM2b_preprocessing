===================
Configuration Files
===================

Perhaps you want to know whether a woman's *weight during the first visit* might be
informative for determining whether or not she develops gestational diabetes later
in her pregnancy.

Weight was recorded in pounds or kilograms, and gestational diabetes is what
we want to predict. We need to:

1. Convert weight to a common unit (we will use pounds here)
2. Combine the two measurements into a single measurement of weight
3. Compare this relation with gestational diabetes

Each of these may be defined as options in a configuration file. The configuration
files here are written in JSON (JavaScript Object Notation). JSON itself is
not fully covered here (there are many tutorials elsewhere online), but the main ideas
should be fairly straightforward after seeing a few examples.

We'll begin with a skeleton and build toward a file with everything we need. This file
does not work yet, but shows us all the keys that we will need to work with.

.. code-block:: json

    {
        "comments": ["comments are ignored."],
        "log_file": "debug.log",
        "csv_path": "../FullData/numom_data/",
        "target": {},
        "files": [],
        "groupings": []
    }

Let's start with the ``"target"``. The target is the file that contains information
about what we want to predict. It is described separately from the other files to
make a few things more convenient behind-the-scenes, and to leave room in the future
for possibly defining behavior depending on what is being predicted.

The ``"target"`` key needs two values: ``"name"`` and ``"variables"``. These allow
us to specify where the file is (relative to the ``"csv_path"``) and what variables
we want to include.

``oDM`` indicates whether the woman developed gestational diabetes, and
``"PublicID"`` is a primary key which identifies her across records.

.. code-block:: json

    {
        "comments": ["comments are ignored."],
        "log_file": "debug.log",
        "csv_path": "../FullData/numom_data/",
        "target": {
            "name": "Ancillary/Pregnancy_outcomes.csv",
            "variables": ["PublicID", "oDM"]
        },
        "files": [],
        "groupings": []
    }

Adding this to ``example_config.json`` is enough to produce a ``data.csv`` when we
run the script as a command-line module.

.. code-block:: bash

    $ python -m numom2b_preprocessing -c example_config.json

.. code-block:: text

    oDM
    3.0
    1.0
    3.0
    2.0

Let's modify the ``"files"`` key to include the variables for weight. There are two
variables that encode this measure, "V1BA01_KG" when weight was recorded in kilograms
and "V1BA01_LB" when weight was recorded in pounds. Once again we include "PublicID"
to keep track of which record corresponds to which person.

.. code-block:: json

    {
        "comments": ["comments are ignored."],
        "log_file": "debug.log",
        "csv_path": "../FullData/numom_data/",
        "target": {
            "name": "Ancillary/Pregnancy_outcomes.csv",
            "variables": ["PublicID", "oDM"]
        },
        "files": [
            {
                "name": "Screening_Admin_Visits/Visit1.csv",
                "variables": ["PublicID", "V1BA01_KG", "V1BA01_LB"]
            }
        ],
        "groupings": []
    }

.. code-block:: bash

    $ python -m numom2b_preprocessing -c example_config.json

.. code-block:: text

    oDM,V1BA01_KG,V1BA01_LB
    3.0,NaN,180
    1.0,NaN,130
    3.0,NaN,144
    2.0,76,NaN

Now that we have the variables we want, we can use the ``"groupings"`` section to convert
them to common units. Operations defined in the ``"groupings"`` section are executed from
top to bottom.

First, we multiply the ``"V1BA01_KG"`` variable by 2.20462, which converts the measurements to
pounds. Then, we take the last measurement between ``"V1BA01_LB"`` and ``"V1BA01_KG"``, then
place the result (``"rename"``) into a new ``"V1BA01"`` variable.

This can be written as follows:

.. code-block:: json

    {
      "comments": ["comments are ignored."],
      "log_file": "debug.log",
      "csv_path": "../FullData/numom_data/",
      "target": {
          "name": "Ancillary/Pregnancy_outcomes.csv",
          "variables": ["PublicID", "oDM"]
      },
      "files": [
        {
          "name": "Screening_Admin_Visits/Visit1.csv",
          "variables": ["PublicID", "V1BA01_KG", "V1BA01_LB"]
        }
      ],
      "groupings": [
        {
          "operator": "multiply_constant",
          "columns": ["V1BA01_KG"],
          "constant": 2.20462
        },
        {
          "operator": "last",
          "columns": ["V1BA01_LB", "V1BA01_KG"],
          "rename": "V1BA01"
        }
      ]
    }

.. code-block:: bash

    $ python -m numom2b_preprocessing -c example_config.json

.. code-block:: text

    oDM,V1BA01
    3.0,180
    1.0,130
    3.0,144
    2.0,167.551

Generalizing from this example, configuration files allow us to specify:

1. The variables of interest
2. Where those variables are located
3. How to transform and aggregate the variables

What is Next?
-------------

The outcome from ``nuMoM2b_preprocessing`` is a ``data.csv`` file. The exact types of machine
learning or statistical modeling you perform next is up to you.
