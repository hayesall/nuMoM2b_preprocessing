# Copyright 2019 Alexander L. Hayes

"""
================
preprocessing.py
================

A script for aligning the columns of the Gestational Diabetes data.

Assumes that a Data folder exists.
"""

import logging

import pandas as pd

LOGGER = logging.getLogger(__name__)

# import data files based on get_config.parameters()
def run(config_parameters):
    """
    Run the preprocessing script based on config parameters.

    ``conf_parameters`` should be passed from get_config.parameters()
    """

    LOGGER.debug("Target File {0}".format(config_parameters["target"]))
    LOGGER.debug("Data Paths {0}".format(config_parameters["paths"]))

    # Start by reading the target csv file.
    target = pd.read_csv(config_parameters["target"])

    # Repeatedly read and inner-join on all data files.
    for _csv_path in config_parameters["paths"]:

        _csv_data = pd.read_csv(_csv_path, sep=",")
        target = pd.merge(target, _csv_data, how="inner", on=["PublicID"])

    return target


if __name__ == "__main__":
    raise Exception("{0} should not be ran from __main__".format(__file__))
