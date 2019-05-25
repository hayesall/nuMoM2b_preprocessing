# Copyright © 2019 Alexander L. Hayes

"""
Test test variable/column cleaning with default values.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import numpy as np
import unittest

# Tests for:
from ... import preprocess


class CleanDefaultValueSingleColumnTests(unittest.TestCase):
    """
    Tests for the ``preprocess._clean_variables`` module.
    """

    @staticmethod
    def test_clean_default_1():
        """
        Test cleaning a single column with no NaN values.
        """
        _table_1 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [np.nan, np.nan, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [np.nan, np.nan, np.nan],
            }
        )

        _cleanings = [{"columns": ["a"], "default_value": 0.0}]
        _table = preprocess._clean_variables(_table_1, _cleanings)

        assert_frame_equal(_table, _table_1)

    @staticmethod
    def test_clean_default_2():
        """
        Test cleaning a single column with some NaN values.
        """
        _table_1 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [np.nan, np.nan, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [np.nan, np.nan, np.nan],
            }
        )

        _cleanings = [{"columns": ["b"], "default_value": 0.0}]
        _expected = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [0.0, 0.0, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [np.nan, np.nan, np.nan],
            }
        )
        _table = preprocess._clean_variables(_table_1, _cleanings)

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_clean_default_3():
        """
        Test cleaning a single column with all NaN values.
        """
        _table_1 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [np.nan, np.nan, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [np.nan, np.nan, np.nan],
            }
        )

        _cleanings = [{"columns": "d", "default_value": 0.0}]
        _expected = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [np.nan, np.nan, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [0.0, 0.0, 0.0],
            }
        )
        _table = preprocess._clean_variables(_table_1, _cleanings)

        assert_frame_equal(_expected, _table)


class CleanDefaultValueMultipleColumnTests(unittest.TestCase):
    """
    Tests for the ``preprocess._clean_variables`` module.
    """

    @staticmethod
    def test_clean_multiple_default_1():
        """
        Test cleaning two columns with no NaN values.
        """
        _table_1 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [np.nan, np.nan, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [np.nan, np.nan, np.nan],
            }
        )

        _cleanings = [{"columns": ["a", "c"], "default_value": 0.0}]
        _expected = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [np.nan, np.nan, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [np.nan, np.nan, np.nan],
            }
        )
        _table = preprocess._clean_variables(_table_1, _cleanings)

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_clean_multiple_default_2():
        """
        Test cleaning two columns where only one has NaN values.
        """
        _table_1 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [np.nan, np.nan, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [np.nan, np.nan, np.nan],
            }
        )

        _cleanings = [{"columns": ["a", "b"], "default_value": 1.0}]
        _expected = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [1.0, 1.0, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [np.nan, np.nan, np.nan],
            }
        )
        _table = preprocess._clean_variables(_table_1, _cleanings)

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_clean_multiple_default_3():
        """
        Test cleaning two columns where both have NaN values.
        """
        _table_1 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [np.nan, np.nan, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [np.nan, np.nan, np.nan],
            }
        )

        _cleanings = [{"columns": ["b", "d"], "default_value": 2.0}]
        _expected = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [2.0, 2.0, 3.0],
                "c": [1.0, 4.0, 5.0],
                "d": [2.0, 2.0, 2.0],
            }
        )
        _table = preprocess._clean_variables(_table_1, _cleanings)

        assert_frame_equal(_expected, _table)
