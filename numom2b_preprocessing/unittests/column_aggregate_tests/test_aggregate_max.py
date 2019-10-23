# Copyright © 2019 Alexander L. Hayes

"""
Tests for the ``aggregate_columns._max`` module.
"""

# TODO(@hayesall): max with np.nan values
# TODO(@hayesall): max of empty data frame
# TODO(@hayesall): max with strings / objects

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...aggregate_columns import ColumnAggregator


class PreprocessMaxTests(unittest.TestCase):
    """
    Tests for the ``aggregate_columns.ColumnAggregator._max`` module. Assert final data frames match expectations.
    """

    @staticmethod
    def test_aggregate_max_1():
        """Test taking the max of one column."""
        _input_1 = DataFrame({"ID": [0, 1, 2, 3], "a": [4.0, 3.0, 2.0, 1.0], "b": [10.0, 9.0, 8.0, 7.0]})
        _expected = DataFrame({"ID": [0, 1, 2, 3], "b": [10.0, 9.0, 8.0, 7.0], "max_a": [4.0, 3.0, 2.0, 1.0]})

        _groupings = [{"operator": "max", "columns": ["a"], "rename": "max_a"}]
        _ca = ColumnAggregator(_input_1)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_max_2():
        """Test taking the max of two columns."""
        _input_2 = DataFrame({"a": [0.0, 0.0, 0.0], "b": [1.0, 2.0, 3.0]})
        _expected = DataFrame({"max_ab": [1.0, 2.0, 3.0]})

        _groupings = [{"operator": "max", "columns": ["a", "b"], "rename": "max_ab"}]
        _ca = ColumnAggregator(_input_2)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_max_3():
        """Test taking the max of three columns."""
        _input_3 = DataFrame({"ID": [0, 1, 2], "a": [0.0, 1.0, 2.0], "b": [1.0, 0.0, 2.0], "c": [2.0, 1.0, 0.0]})
        _expected = DataFrame({"ID": [0, 1, 2], "MAX_ABC": [2.0, 1.0, 2.0]})

        _groupings = [{"operator": "max", "columns": ["a", "b", "c"], "rename": "MAX_ABC"}]
        _ca = ColumnAggregator(_input_3)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_max_different_types():
        """Test taking the max of two columns with int/float types."""
        _input_4 = DataFrame({"ID": [0, 1, 2], "a": [0, 1, 0], "b": [0.0, 3.0, -1.0]})
        _expected = DataFrame({"ID": [0, 1, 2], "max_ab": [0.0, 3.0, 0.0]})

        _groupings = [{"operator": "max", "columns": ["a", "b"], "rename": "max_ab"}]
        _ca = ColumnAggregator(_input_4)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)
