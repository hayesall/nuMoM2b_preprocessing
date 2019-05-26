# Copyright © 2019 Alexander L. Hayes

"""
Tests for the variable/column cleaning with variable dropping on "!="
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ... import preprocess


class CleanDropIfLessThanTests(unittest.TestCase):
    """
    Tests for the ``preprocess._clean_variables`` module dropping rows "<"
    """

    @staticmethod
    def test_drop_if_less_than_1():
        """
        Test that no rows are dropped if conditions are not met.
        """
        _table_1 = DataFrame(
            {
                "a": [1, 2, 3, 4],
                "b": [2, 3, 4, 5]
            }
        )

        _cleanings = [{"columns": ["a"], "drop_if": ["<", 0.0]}]
        _table = preprocess._clean_variables(_table_1, _cleanings)

        assert_frame_equal(_table, _table_1)

    @staticmethod
    def test_drop_if_less_than_2():
        """
        Test that a single row is dropped.
        """
        _table_2 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [3.0, 4.0, 5.0],
            }
        )

        _cleanings = [{"columns": ["a"], "drop_if": ["<", 2.0]}]
        _expected = DataFrame(
            {
                "a": [2.0, 3.0],
                "b": [4.0, 5.0],
            }
        )
        _table = preprocess._clean_variables(_table_2, _cleanings)

        # TODO: This is a hack for row indexes
        _expected.index = _table.index

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_drop_if_less_than_3():
        """
        Test that no rows are dropped when the condition is met in another row.
        """
        _table_3 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [3.0, 4.0, 5.0],
            }
        )
        _cleanings = [{"columns": ["b"], "drop_if": ["<", 3.0]}]
        _table = preprocess._clean_variables(_table_3, _cleanings)

        assert_frame_equal(_table, _table_3)

    @staticmethod
    def test_drop_if_less_than_4():
        """
        Test that everything is dropped.
        """
        _table_4 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0],
                "b": [3.0, 4.0, 5.0],
            }
        )

        _cleanings = [{"columns": ["a"], "drop_if": ["<", 5.0]}]
        _expected = DataFrame(
            {
                "a": [],
                "b": [],
            }
        )
        _table = preprocess._clean_variables(_table_4, _cleanings)

        # TODO: This is a hack for row indexes
        _expected.index = _table.index

        assert_frame_equal(_expected, _table)

    def test_drop_if_less_than_5(self):
        """
        Test that an error is raised when multiple columns are passed.
        """
        _table_5 = DataFrame(
            {
                "a": [3.0, 4.0, 5.0, 6.0],
                "b": [3.0, 7.0, 9.0, 6.0],
            }
        )
        _cleanings = [{"columns": ["a", "b"], "drop_if": ["<", 3.0]}]

        with self.assertRaises(Exception):
            _table = preprocess._clean_variables(_table_5, _cleanings)
