# Copyright 2019 Alexander L. Hayes

"""
Create reproducible partitions of the nuMoM2b data set based on
configuration files.
"""

import argparse
import logging

from ._meta import __version__, __copyright__, __license__, __email__
from . import get_config
from . import preprocess

# Argument Parser

PARSER = argparse.ArgumentParser(
    prog="nuMoM2b_preprocessing@{0}".format(__version__),
    description=__doc__,
    epilog="{0} ({1}). Distributed under the terms of the {2} License.".format(
        __copyright__, __email__, __license__
    ),
)
PARSER.add_argument(
    "-c",
    "--config",
    type=str,
    default="phi_config.json",
    help="Set the configuration file to read from [Default:phi_config.json].",
)
PARSER.add_argument(
    "-l",
    "--logging",
    type=int,
    default=10,  # logging.DEBUG
    help="Set the verbosity of the Python logger [Default:10]. Follows Logging Levels.",
)
PARSER.add_argument(
    "-o",
    "--output",
    type=str,
    default="data.csv",
    help="File name to write output to [Default:data.csv].",
)
PARSER.add_argument(
    "-t",
    "--test",
    action="store_true",
    help="Display information for unit tests, code coverage, and formatting.",
)
PARSER.add_argument(
    "--drop-nan", action="store_true", help="Drop rows containing NaN values."
)

# Data Section

TEST_INFO = """=============
Code Quality:
=============

Unit testing and code coverage are evaluated using ``coverage``. Linting is
performed with ``pylint`` and style is enforced with ``black``.

Installation
------------

.. code-block:: bash

    pip install coverage black pylint

Unit Tests
----------

Unit tests can be a relatively easy check for everything being in working order
or whether any assumptions are violated.

From the base of the repository:

.. code-block:: bash

    coverage run numom2b_preprocessing/unittests/tests.py
    coverage html
    open htmlcov/index.html
"""

# Arguments and Configuration Files

ARGS = PARSER.parse_args()
PARAMETERS = get_config.parameters(config=ARGS.config)

# Initialize logging options

LOGFILE = PARAMETERS["log_file"] if PARAMETERS.get("log_file") else "debug.log"

logging.basicConfig(
    filename="{0}".format(LOGFILE),
    level=ARGS.logging,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
LOGGER = logging.getLogger(__name__)

LOGGER.info("Starting the logger.")

# Logic for Running

if ARGS.test:
    LOGGER.info("Displaying test information for user.")
    print(TEST_INFO)
    LOGGER.info("Reached bottom, shutting down logger.")
    exit(0)

LOGGER.info("Pre-processing the data.")

DATA = preprocess.run(PARAMETERS)

LOGGER.info("Completed pre-processing.")

# Drop the PublicID Column for learning/inference
LOGGER.info("Dropping `PublicID` column for learning/inference.")
DATA = DATA.drop("PublicID", axis=1)

if ARGS.drop_nan:
    LOGGER.info("Dropping NaN rows.")
    DATA = DATA.dropna()

# Write to csv
LOGGER.info("Writing data to file " + ARGS.output)
DATA.to_csv(ARGS.output, index=False, na_rep="NaN")
LOGGER.info("Done writing data to file " + ARGS.output)

LOGGER.info("Reached bottom, shutting down logger.")
logging.shutdown()
exit(0)
