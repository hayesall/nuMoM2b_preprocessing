# Copyright 2019 Alexander L. Hayes

"""
Test for the ``preprocess._aggregate_columns`` (count) module.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
from numpy import float64
import unittest

# Tests for:
from ... import aggregate_columns


class PreprocessCountTests(unittest.TestCase):
    """
    Tests for the ``aggregate_columns.ColumnAggregator._count`` module. Assert final data frames match expectations.
    """

    @staticmethod
    def test_aggregate_count_columns_1():
        """
        Test aggregating with the "last" operation on an example DataFrame.
        """

        _input_table = DataFrame(
            {
                "ID": [0, 1, 1, 2],
                "a": [float64("nan"), float64("nan"), float64("nan"), float64("nan")],
                "b": [2, 3, 4, 5],
            }
        )
        _groupings = [{"operator": "count", "columns": ["a", "b"]}]
        _expected = DataFrame({"ID": [0, 1, 1, 2], "countab": [1, 1, 1, 1]})

        _ca = aggregate_columns.ColumnAggregator(_input_table)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_count_columns_2():
        """
        Test counting columns of strings when there are no missing values.
        """

        _input_table = DataFrame(
            {"ID": ["a", "b", "c"], "a": ["a", "b", "c"], "b": ["a", "b", "c"]}
        )
        _groupings = [{"operator": "count", "columns": ["a", "b"]}]
        _expected = DataFrame({"ID": ["a", "b", "c"], "countab": [2, 2, 2]})

        _ca = aggregate_columns.ColumnAggregator(_input_table)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_count_columns_3():
        """
        Test counting columns of integers with missing values at the beginning.
        """

        _input_table = DataFrame(
            {
                "PublicID": [4, 3, 2, 1, 0],
                "5": [
                    float64("nan"),
                    float64("nan"),
                    float64("nan"),
                    float64("nan"),
                    float64("nan"),
                ],
                "4": [
                    float64("nan"),
                    float64("nan"),
                    float64("nan"),
                    float64("nan"),
                    float64(10000),
                ],
                "3": [
                    float64("nan"),
                    float64("nan"),
                    float64("nan"),
                    float64(30000),
                    float64(20000),
                ],
                "2": [
                    float64("nan"),
                    float64("nan"),
                    float64(50000),
                    float64(40000),
                    float64(30000),
                ],
                "1": [
                    float64("nan"),
                    float64(70000),
                    float64(60000),
                    float64(50000),
                    float64(40000),
                ],
            }
        )
        _groupings = [{"operator": "count", "columns": ["5", "4", "3", "2", "1"]}]
        _expected = DataFrame(
            {"PublicID": [4, 3, 2, 1, 0], "count54321": [0, 1, 2, 3, 4]}
        )

        _ca = aggregate_columns.ColumnAggregator(_input_table)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_count_columns_4():
        """
        Test aggregating with the "last" operation on an example DataFrame using _count.
        """

        _input_table = DataFrame(
            {
                "ID": [0, 1, 1, 2],
                "a": [float64("nan"), float64("nan"), float64("nan"), float64("nan")],
                "b": [2, 3, 4, 5],
            }
        )
        _groupings = [{"operator": "count", "columns": ["a", "b"]}]
        _expected = DataFrame({"ID": [0, 1, 1, 2], "countab": [1, 1, 1, 1]})

        _ca = aggregate_columns.ColumnAggregator(_input_table)
        _ca._count(["a", "b"], "countab")

        assert_frame_equal(_expected, _ca.frame)
