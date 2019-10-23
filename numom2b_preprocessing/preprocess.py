# Copyright 2019 Alexander L. Hayes

"""
Combine and aggregate columns across tables.
"""

from .aggregate_columns import ColumnAggregator
from .clean_variables import VariableCleaner
from .row_filter import RowFilter
import logging
import pandas as pd

LOGGER = logging.getLogger(__name__)


def run(config_parameters):
    """
    :return: pandas.core.frame.DataFrame

    Preprocess the data according to the configuration parameters.

    ``conf_parameters`` should be passed from :meth:`numom2b_preprocessing.get_config.parameters`
    """

    _table = _build_table(config_parameters)

    if config_parameters.get("clean_variables"):
        _vc = VariableCleaner(_table)
        _vc.clean(config_parameters["clean_variables"])
        _table = _vc.frame

    if config_parameters.get("groupings"):

        print(
            "Deprecation Warning: 'groupings' will be removed in 0.3.0. Use 'aggregate_columns' instead.'"
        )
        LOGGER.warning(
            "Deprecation Warning: 'groupings' will be removed in 0.3.0. Use 'aggregate_columns' instead.'"
        )

        _ca = ColumnAggregator(_table)
        _ca.aggregate(config_parameters["groupings"])
        _table = _ca.frame

    if config_parameters.get("aggregate_columns"):
        _ca = ColumnAggregator(_table)
        _ca.aggregate(config_parameters["aggregate_columns"])
        _table = _ca.frame

    if config_parameters.get("filter"):
        _rf = RowFilter(_table)
        _rf.filter(config_parameters["filter"])
        _table = _rf.frame

    return _table


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


def _build_target_table(file_name, columns):
    """
    :return: pandas.core.frame.DataFrame
    """

    target = pd.read_csv(file_name, sep=",")
    _log_columns(file_name, str(list(target.columns)))
    target = target[columns]
    _log_columns(file_name, str(list(target.columns)))

    return target


def _build_table(config_parameters):
    """
    Repeatedly read, drop, and inner-join on all files.

    :return: pandas.core.frame.DataFrame
    """

    LOGGER.debug("Target File {0}".format(config_parameters["target"]))
    LOGGER.debug("Data Paths {0}".format(config_parameters["paths"]))

    _name = config_parameters["target"][0]
    _variables = config_parameters["target"][1]

    target = _build_target_table(_name, _variables)

    for _data_tuple in config_parameters["paths"]:

        _name, _variables = _data_tuple[0], _data_tuple[1]

        _csv_data = pd.read_csv(_name, sep=",", engine="python")
        _log_columns(_name, str(list(_csv_data.columns)))
        _csv_data = _csv_data[_variables]
        _log_columns(_name, str(list(_csv_data.columns)))

        target = pd.merge(target, _csv_data, how="inner", on=["PublicID"])

    return target


if __name__ == "__main__":
    raise Exception("{0} should not be ran from __main__".format(__file__))
