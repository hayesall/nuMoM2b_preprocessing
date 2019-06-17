# Copyright © 2019 Alexander L. Hayes

"""
Tests for the variable/column cleaning with variable dropping on "!="
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...row_filter import RowFilter


class CleanDropIfLessThanTests(unittest.TestCase):
    """
    Tests for the ``preprocess._clean_variables`` module dropping rows "<"
    """

    @staticmethod
    def test_drop_if_less_than_1():
        """
        Test that no rows are dropped if conditions are not met.
        """
        _table_1 = DataFrame({"a": [1, 2, 3, 4], "b": [2, 3, 4, 5]})

        _cleanings = [{"operator": "drop_if_less_than", "columns": ["a"], "value": 0.0}]
        _rf = RowFilter(_table_1)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_1, _rf.frame)

    @staticmethod
    def test_drop_if_less_than_2():
        """
        Test that a single row is dropped.
        """
        _table_2 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [3.0, 4.0, 5.0]})

        _cleanings = [{"operator": "drop_if_less_than", "columns": ["a"], "value": 2.0}]
        _expected = DataFrame({"a": [2.0, 3.0], "b": [4.0, 5.0]})
        _rf = RowFilter(_table_2)
        _rf.filter(_cleanings)

        # TODO: This is a hack for row indexes
        _expected.index = _rf.frame.index

        assert_frame_equal(_expected, _rf.frame)

    @staticmethod
    def test_drop_if_less_than_3():
        """
        Test that no rows are dropped when the condition is met in another row.
        """
        _table_3 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [3.0, 4.0, 5.0]})
        _cleanings = [{"operator": "drop_if_less_than", "columns": ["b"], "value": 3.0}]
        _rf = RowFilter(_table_3)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_3, _rf.frame)

    @staticmethod
    def test_drop_if_less_than_4():
        """
        Test that everything is dropped.
        """
        _table_4 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [3.0, 4.0, 5.0]})

        _cleanings = [{"operator": "drop_if_less_than", "columns": ["a"], "value": 5.0}]
        _expected = DataFrame({"a": [], "b": []})
        _rf = RowFilter(_table_4)
        _rf.filter(_cleanings)

        # TODO: This is a hack for row indexes
        _expected.index = _rf.frame.index

        assert_frame_equal(_expected, _rf.frame)

    def test_drop_if_less_than_5(self):
        """
        Test that an error is raised when multiple columns are passed.
        """
        _table_5 = DataFrame({"a": [3.0, 4.0, 5.0, 6.0], "b": [3.0, 7.0, 9.0, 6.0]})
        _cleanings = [
            {"operator": "drop_if_less_than", "columns": ["a", "b"], "value": 3.0}
        ]

        _rf = RowFilter(_table_5)
        with self.assertRaises(Exception):
            _rf.filter(_cleanings)
