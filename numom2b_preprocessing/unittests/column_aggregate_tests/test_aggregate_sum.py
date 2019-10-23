# Copyright © 2019 Alexander L. Hayes

"""
Tests for the ``aggregate_columns._sum`` module.
"""

# TODO(@hayesall): Sum with np.nan values.

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...aggregate_columns import ColumnAggregator


class PreprocessSumTests(unittest.TestCase):
    """
    Tests for the ``aggregate_columns.ColumnAggregator._sum`` module. Assert final data match expectations.
    """

    @staticmethod
    def test_aggregate_sum_1():
        """Test taking the sum of one column."""
        _input_1 = DataFrame({"a": [0, 0, 0]})
        _expected = DataFrame({"sum_a": [0, 0, 0]})

        _groupings = [{"operator": "sum", "columns": ["a"], "rename": "sum_a"}]
        _ca = ColumnAggregator(_input_1)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_sum_2():
        """Test taking the sum of two columns."""
        _input_2 = DataFrame({"a": [0, 1, 2], "b": [2, 1, 0]})
        _expected = DataFrame({"sum_ab": [2, 2, 2]})

        _groupings = [{"operator": "sum", "columns": ["a", "b"], "rename": "sum_ab"}]
        _ca = ColumnAggregator(_input_2)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)

    @staticmethod
    def test_aggregate_sum_3():
        """Test taking the sum of three columns."""
        _input_3 = DataFrame({"A": [3.0, 1.0], "B": [4.0, 0.0], "C": [4.5, 5.5]})
        _expected = DataFrame({"Sum_ABC": [11.5, 6.5]})

        _groupings = [{"operator": "sum", "columns": ["A", "B", "C"], "rename": "Sum_ABC"}]
        _ca = ColumnAggregator(_input_3)
        _ca.aggregate(_groupings)

        assert_frame_equal(_expected, _ca.frame)
