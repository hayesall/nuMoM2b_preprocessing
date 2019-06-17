# Copyright 2019 Alexander L. Hayes

"""
Conditionally filter rows.
"""

import logging
import numpy as np
import pandas as pd

LOGGER = logging.getLogger(__name__)


class RowFilter:
    """
    Filter rows from a DataFrame.
    """

    def __init__(self, data_frame):
        self.frame = data_frame

    def filter(self, operations_list):
        """
        :param operations_list: List of dictionaries with 'operator' and 'columns' keys.
        """

        LOGGER.debug("Starting row filtering.")

        # TODO: Conditions for handling null values.

        operations = {
            "drop_if_equal": self._equal,
            "drop_if_not_equal": self._not_equal,
            "drop_if_greater": self._greater_than,
            "drop_if_less_than": self._less_than,
        }

        for aggregation in operations_list:
            _operation = aggregation["operator"]
            _columns = aggregation["columns"]
            _value = aggregation["value"]

            LOGGER.debug("{0},{1},{2}".format(_operation, str(_columns), _value))
            operations[_operation](_columns, _value)

        LOGGER.debug("Finished row filtering.")

    def _equal(self, columns, value):
        if len(columns) > 1:
            raise Exception(
                "Cannot use 'drop_if_equal' with multiple columns: ", columns
            )
        self.frame = self.frame.drop(np.flatnonzero(self.frame[columns] == value))

    def _not_equal(self, columns, value):
        if len(columns) > 1:
            raise Exception(
                "Cannot use 'drop_if_not_equal' with multiple columns: ", columns
            )
        self.frame = self.frame.drop(np.flatnonzero(self.frame[columns] != value))

    def _greater_than(self, columns, value):
        if len(columns) > 1:
            raise Exception(
                "Cannot use 'drop_if_greater' with multiple columns: ", columns
            )
        self.frame = self.frame.drop(np.flatnonzero(self.frame[columns] > value))

    def _less_than(self, columns, value):
        if len(columns) > 1:
            raise Exception(
                "Cannot use 'drop_if_less_than' with multiple columns: ", columns
            )
        self.frame = self.frame.drop(np.flatnonzero(self.frame[columns] < value))
