# Copyright © 2019 Alexander L. Hayes

"""
Tests for the ``aggregate_columns._min`` module.
"""

# TODO(@hayesall): min with np.nan values
# TODO(@hayesall): min of empty data frame
# TODO(@hayesall): min with strings / objects

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...aggregate_columns import ColumnAggregator


class PreprocessMinTests(unittest.TestCase):
    """
    Tests for the ``aggregate_columns.ColumnAggregator._min`` module. Assert final data frames match expectations.
    """

    @staticmethod
    def test_aggregate_min_1():
        """Test taking the min of one column."""
        _input_1 = DataFrame({"ID": [0, 1, 2, 3], "a": [4.0, 3.0, 2.0, 1.0], "b": [10.0, 9.0, 8.0, 7.0]})
        _expected = DataFrame({"ID": [0, 1, 2, 3], "b": [10.0, 9.0, 8.0, 7.0], "min_a": [4.0, 3.0, 2.0, 1.0]})

        _groupings = [{"operator": "min", "columns": ["a"], "rename": "min_a"}]
        _ca = ColumnAggregator(_input_1)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_min_2():
        """Test taking the min of two columns."""
        _input_2 = DataFrame({"a": [0.0, 0.0, 0.0], "b": [1.0, 2.0, 3.0]})
        _expected = DataFrame({"min_ab": [0.0, 0.0, 0.0]})

        _groupings = [{"operator": "min", "columns": ["a", "b"], "rename": "min_ab"}]
        _ca = ColumnAggregator(_input_2)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_min_3():
        """Test taking the min of three columns."""
        _input_3 = DataFrame({"ID": [0, 1, 2], "a": [0.0, 1.0, 2.0], "b": [1.0, 0.0, 2.0], "c": [2.0, 1.0, 0.0]})
        _expected = DataFrame({"ID": [0, 1, 2], "MIN_ABC": [0.0, 0.0, 0.0]})

        _groupings = [{"operator": "min", "columns": ["a", "b", "c"], "rename": "MIN_ABC"}]
        _ca = ColumnAggregator(_input_3)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_min_different_types():
        """Test taking the min of two columns with int/float types."""
        _input_4 = DataFrame({"ID": [0, 1, 2], "a": [0, 1, 0], "b": [0.0, 3.0, -1.0]})
        _expected = DataFrame({"ID": [0, 1, 2], "min_ab": [0.0, 1.0, -1.0]})

        _groupings = [{"operator": "min", "columns": ["a", "b"], "rename": "min_ab"}]
        _ca = ColumnAggregator(_input_4)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)
