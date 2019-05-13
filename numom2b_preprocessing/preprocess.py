# Copyright 2019 Alexander L. Hayes

"""
Combine and aggregate columns across tables.
"""

import logging
import numpy as np
import pandas as pd

LOGGER = logging.getLogger(__name__)


def run(config_parameters):
    """
    :arg config_parameters:
    :return: pandas.core.frame.DataFrame

    Preprocess the data according to the configuration parameters.

    ``conf_parameters`` should be passed from :meth:`numom2b_preprocessing.get_config.parameters`
    """

    _table = _build_table(config_parameters)

    if config_parameters.get("groupings"):
        _table = _aggregate_columns(_table, config_parameters["groupings"])

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


def _aggregate_columns(data_frame, groupings):
    """
    Mutate the data frame by aggregating columns according to configuration parameters,
    then drop the existing columns.

    :arg ``config_parameters["groupings"]``
    :return: pandas.core.frame.DataFrame
    """

    # TODO: This would make more sense as a class. That way we could do: ``frame.aggregate(operation, columns, rename)``

    LOGGER.debug("Starting aggregation")

    for entry in groupings:

        _operation = entry["operator"]
        _columns = entry["columns"]
        _rename = (
            entry["rename"]
            if entry.get("rename")
            else "{0}{1}".format(entry["operator"], str("".join(entry["columns"])))
        )

        LOGGER.debug(
            "{0} (operator), {1} (columns), {2} (rename-to)".format(
                _operation, str(_columns), _rename
            )
        )

        if _operation == "multiply_constant":

            # "rename" is not used in "multiply_constant"

            # "multiply_constant" must be accompanied by a constant
            _constant = entry["constant"]

            data_frame[_columns] = (
                data_frame[_columns]
                .replace(["D", "S"], np.float("nan"))
                .astype("float64")
                * _constant
            )

        if _operation == "mean":

            data_frame[_rename] = np.mean(data_frame[_columns], axis=1)
            data_frame = data_frame.drop(_columns, axis=1)

        if _operation == "last":

            data_frame[_rename] = data_frame[_columns].ffill(axis=1).iloc[:, -1]
            data_frame = data_frame.drop(_columns, axis=1)

        if _operation == "count":

            data_frame[_rename] = data_frame[_columns].count(axis="columns")
            data_frame = data_frame.drop(_columns, axis=1)

        if _operation == "normalized_difference":

            # _columns[A, B, C] --> (A - B) / C
            # Normalize a column with respect to a third column.

            _A = (
                data_frame[_columns[0]]
                .replace(["D", "S"], np.float("nan"))
                .astype("float64")
            )
            _B = (
                data_frame[_columns[1]]
                .replace(["D", "S"], np.float("nan"))
                .astype("float64")
            )
            _C = (
                data_frame[_columns[2]]
                .replace(["D", "S"], np.float("nan"))
                .astype("float64")
            )

            data_frame[_rename] = (_A - _B) / _C

    LOGGER.debug("Finished aggregation")
    return data_frame


def _build_target_table(file_name, columns):
    """
    :param file_name:
    :param columns_to_drop:
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
