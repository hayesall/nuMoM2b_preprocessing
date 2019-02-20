# Copyright 2019 Alexander L. Hayes

"""
Test for the ``preprocess._aggregate_columns`` (mean) module.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ... import preprocess


class PreprocessMeanTests(unittest.TestCase):
    """
    Tests for the ``preprocess._aggregate_columns`` module. Assert final data frames match expectations.
    """

    @staticmethod
    def test_aggregate_mean_columns_1():
        """
        Test aggregating with the "mean" operation over two columns on an example DataFrame.
        """

        _input_table = DataFrame(
            {"ID": [0, 1, 1, 2], "a": [1, 2, 3, 4], "b": [2, 3, 4, 5]}
        )
        _groupings = [{"operator": "mean", "columns": ["a", "b"]}]
        _expected = DataFrame({"ID": [0, 1, 1, 2], "meanab": [1.5, 2.5, 3.5, 4.5]})
        _table = preprocess._aggregate_columns(_input_table, _groupings)

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_aggregate_mean_columns2():
        """
        Test aggregating with the "mean" operation over three columns on an example DataFrame.
        """

        _input_table = DataFrame(
            {
                "ID": [0, 1, 1, 2],
                "a": [1, 2, 3, 4],
                "b": [2, 3, 4, 5],
                "c": [3, 4, 5, 6],
            }
        )
        _groupings = [{"operator": "mean", "columns": ["a", "b", "c"], "rename": "d"}]
        _expected = DataFrame({"ID": [0, 1, 1, 2], "d": [2.0, 3.0, 4.0, 5.0]})
        _table = preprocess._aggregate_columns(_input_table, _groupings)

        assert_frame_equal(_expected, _table)
