# Copyright 2019 Alexander L. Hayes

"""
Test for the ``aggregate_columns.ColumnAggregator._mean`` module.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ... import aggregate_columns


class PreprocessMeanTests(unittest.TestCase):
    """
    Tests for the ``aggregate_columns.ColumnAggregator._mean`` module. Assert final data frames match expectations.
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

        _ca = aggregate_columns.ColumnAggregator(_input_table)
        _ca.aggregate(_groupings)
        assert_frame_equal(_expected, _ca.frame)

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

        _ca = aggregate_columns.ColumnAggregator(_input_table)
        _ca.aggregate(_groupings)
        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_mean_columns3():
        """
        Test aggregating using the _mean function.
        """

        _input_table = DataFrame(
            {"ID": [0, 1, 1, 2], "a": [1, 2, 3, 4], "b": [2, 3, 4, 5]}
        )
        _expected = DataFrame({"ID": [0, 1, 1, 2], "meanab": [1.5, 2.5, 3.5, 4.5]})

        _ca = aggregate_columns.ColumnAggregator(_input_table)
        _ca._mean(["a", "b"], "meanab")
        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_mean_columns4():
        """
        Test aggregating with the "mean" operation over three columns on an example DataFrame
        using the _mean function.
        """

        _input_table = DataFrame(
            {
                "ID": [0, 1, 1, 2],
                "a": [1, 2, 3, 4],
                "b": [2, 3, 4, 5],
                "c": [3, 4, 5, 6],
            }
        )
        _expected = DataFrame({"ID": [0, 1, 1, 2], "d": [2.0, 3.0, 4.0, 5.0]})

        _ca = aggregate_columns.ColumnAggregator(_input_table)
        _ca._mean(["a", "b", "c"], "d")
        assert_frame_equal(_expected, _ca.frame)
