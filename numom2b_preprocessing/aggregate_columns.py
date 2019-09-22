# Copyright 2019 Alexander L. Hayes

"""
Aggregate columns.
"""

import logging
import numpy as np
import pandas as pd

LOGGER = logging.getLogger(__name__)


class ColumnAggregator:
    """
    Mutate a data frame according to configuration parameters.
    Drop the modified columns.
    """

    def __init__(self, data_frame):
        self.frame = data_frame

    def aggregate(self, operations_list):
        """
        Mutate a data frame according to configuration parameters.

        :param operations_list: List of dictionaries with 'operator' and 'columns' keys.

        Examples:

        >>> data_frame = pd.DataFrame({"ID": [0, 1, 2], "a": [3.3, 4.5, 1.2], "b": [3, 2, 4})
        >>> ca = ColumnAggregator()
        >>> ca.aggregate(
        ...     [
        ...         {
        ...             "operator": "mean",
        ...             "columns": ["a, "b"],
        ...             "rename": "mean_a_b",
        ...         },
        ...     ],
        ... )
        """
        LOGGER.debug("Starting column aggregation.")

        operations = {
            "mean": self._mean,
            "last": self._last,
            "count": self._count,
            "max": self._max,
            "sum": self._sum,
        }

        for aggregation in operations_list:
            _operation = aggregation["operator"]
            _columns = aggregation["columns"]
            _rename = (
                aggregation["rename"]
                if aggregation.get("rename")
                else "{0}{1}".format(
                    aggregation["operator"], str("".join(aggregation["columns"]))
                )
            )

            LOGGER.debug("{0},{1},{2}".format(_operation, str(_columns), _rename))
            operations[_operation](_columns, _rename)

        LOGGER.debug("Finished column aggregation.")

    def _sum(self, columns, rename):
        self.frame[rename] = np.sum(self.frame[columns], axis=1)
        self.frame = self.frame.drop(columns, axis=1)

    def _max(self, columns, rename):
        self.frame[rename] = np.max(self.frame[columns], axis=1)
        self.frame = self.frame.drop(columns, axis=1)

    def _mean(self, columns, rename):
        self.frame[rename] = np.mean(self.frame[columns], axis=1)
        self.frame = self.frame.drop(columns, axis=1)

    def _last(self, columns, rename):
        self.frame[rename] = self.frame[columns].ffill(axis=1).iloc[:, -1]
        self.frame = self.frame.drop(columns, axis=1)

    def _count(self, columns, rename):
        self.frame[rename] = self.frame[columns].count(axis="columns")
        self.frame = self.frame.drop(columns, axis=1)
