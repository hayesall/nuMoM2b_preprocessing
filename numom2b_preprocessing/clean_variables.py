# Copyright 2019 Alexander L. Hayes

"""
Clean individual variables.
"""

import logging
import numpy as np

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
            "replace": self._replace,
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
        try:
            # Default behavior: multiply.
            self.frame[columns] = self.frame[columns] * value
        except TypeError:

            # Try catching a TypeError and converting to float

            try:
                self.frame[columns] = self.frame[columns].astype(float) * value
            except ValueError as _message:
                # ValueError will be thrown if we cannot convert to float

                LOGGER.error("Error: {0} in (columns: {1})".format(_message, columns))
                raise RuntimeError(
                    'Could not "multiply_constant" operation on "{0}". Try "default_value" or "replace" first.'.format(
                        columns
                    )
                )

    def _replace(self, columns, value):
        # Replace a specific value with another value.
        self.frame[columns] = self.frame[columns].replace(value[0], value[1])
