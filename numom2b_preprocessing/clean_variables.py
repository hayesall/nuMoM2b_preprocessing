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
        :param operations_list: List of dictionaries with 'operator', 'columns', and 'value' keys.
        """
        LOGGER.debug("Started variable cleaning.")

        operations = {
            "default_value": self._default_value,
            "difference": self._difference,
            "divide": self._divide,
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

    def _divide(self, columns, value):

        if not isinstance(value, str):
            # 'value' is numeric and we should be able to divide by the constant.
            self.frame[columns] = self.frame[columns] / value
        else:

            if len(columns) > 1:
                raise ValueError(
                    '"operation": "divide" with multiple columns as input is ambiguous.'
                )

            # TODO(@hayesall): Catching and throwing custom divide-by-zero errors might make them more readable.
            try:
                self.frame[columns[0]] = self.frame[columns[0]] / self.frame[value]
            except TypeError:
                try:
                    self.frame[columns[0]] = self.frame[columns[0]].astype(float) / self.frame[value].astype(float)
                except ValueError as _message:
                    LOGGER.error(
                        "Error: {0} in (columns: {1})".format(_message, columns)
                    )
                    raise RuntimeError(
                        'Could not complete "divide" operation on "{0}". Try "default_value" or "replace" first.'
                    )

    def _difference(self, columns, value):

        if not isinstance(value, str):
            # 'value' is numeric and we should be able to subtract the constant.
            self.frame[columns] = self.frame[columns] - value
        else:

            if len(columns) > 1:
                raise ValueError(
                    '"operation": "difference" between two columns is ambiguous.'
                )

            try:
                self.frame[columns[0]] = self.frame[columns[0]] - self.frame[value]
            except TypeError:
                try:
                    self.frame[columns[0]] = self.frame[columns[0]].astype(float) - self.frame[value].astype(float)
                except ValueError as _message:
                    LOGGER.error(
                        "Error: {0} in (columns: {1})".format(_message, columns)
                    )
                    raise RuntimeError(
                        'Could not complete "difference" operation on "{0}". Try "default_value" or "replace" first.'.format(
                            columns
                        )
                    )

    def _multiply_constant(self, columns, value):
        # TODO(@hayesall): Generalize to allow multiplying by content of a column.
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
        if value[1] == "NaN":
            self.frame[columns] = self.frame[columns].replace(value[0], np.nan)
        else:
            self.frame[columns] = self.frame[columns].replace(value[0], value[1])
