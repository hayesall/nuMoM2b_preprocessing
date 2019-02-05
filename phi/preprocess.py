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


def _log_columns(csv_path, string_of_columns):
    """
    Log the column names for possible debugging.

    Example:

    .. code-block:: python

        _target = pd.read_csv(config_parameters["target"])
        _target_columns = str(list(target.columns))

        _log_columns(config_parameters["target"], _target_columns)
    """
    LOGGER.debug("File: {0}; Columns: {1}".format(csv_path, string_of_columns))


# import data files based on get_config.parameters()
def run(config_parameters):
    """
    Run the preprocessing script based on config parameters.

    ``conf_parameters`` should be passed from get_config.parameters()
    """

    LOGGER.debug("Target File {0}".format(config_parameters["target"]))
    LOGGER.debug("Data Paths {0}".format(config_parameters["paths"]))

    # Read the target csv and drop any specified columns.
    _name = config_parameters["target"][0]
    _drop = config_parameters["target"][1]

    target = pd.read_csv(_name, sep=",")
    _log_columns(config_parameters["target"][0], str(list(target.columns)))
    target = target.drop(_drop, axis=1)
    _log_columns(config_parameters["target"][0], str(list(target.columns)))

    # Repeatedly read, drop, and inner-join on all data files.
    for _data_tuple in config_parameters["paths"]:

        _name, _drop = _data_tuple[0], _data_tuple[1]

        _csv_data = pd.read_csv(_name, sep=",")
        _log_columns(_name, str(list(_csv_data.columns)))
        _csv_data = _csv_data.drop(_drop, axis=1)
        _log_columns(_name, str(list(_csv_data.columns)))

        target = pd.merge(target, _csv_data, how="inner", on=["PublicID"])

    return target


if __name__ == "__main__":
    raise Exception("{0} should not be ran from __main__".format(__file__))
