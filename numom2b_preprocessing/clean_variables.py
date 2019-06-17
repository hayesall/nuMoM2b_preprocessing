# Copyright 2019 Alexander L. Hayes

"""
Clean individual variables.
"""

import logging
import numpy as np
import pandas as pd

LOGGER = logging.getLogger(__name__)


class VariableCleaner:
    """
    Clean individual variables in-place.
    """

    def __init__(self, data_frame):
        self.frame = data_frame

    def clean(self, operations_list):
        """
        :param operations: List of dictionaries with 'operator', 'columns', and 'value' keys.
        """
        LOGGER.debug("Started variable cleaning.")

        operations = {
            "default_value": self._default_value,
            "multiply_constant": self._multiply_constant,
        }

        for aggregation in operations_list:
            _operation = aggregation["operator"]
            _columns = aggregation["columns"]
            _value = aggregation["value"]

            LOGGER.debug("{0},{1},{2}".format(_operation, _columns, _value))

            operations[_operation](_columns, _value)

        LOGGER.debug("Finished variable cleaning.")

    def _default_value(self, columns, value):
        self.frame[columns] = self.frame[columns].fillna(value)

    def _multiply_constant(self, columns, value):
        self.frame[columns] = self.frame[columns] * value
