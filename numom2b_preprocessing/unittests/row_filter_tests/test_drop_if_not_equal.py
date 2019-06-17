# Copyright © 2019 Alexander L. Hayes

"""
Tests for the variable/column cleaning with variable dropping on "!="
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...row_filter import RowFilter


class CleanDropIfNotEqualTests(unittest.TestCase):
    """
    Tests for the ``preprocess._clean_variables`` module dropping rows based on "!="
    """

    @staticmethod
    def test_drop_if_not_equal_1():
        """
        Test that no rows are dropped if conditions are not met.
        """
        _table_1 = DataFrame({"a": [2.0, 2.0, 2.0], "b": [3.0, 4.0, 5.0]})

        _cleanings = [{"operator": "drop_if_not_equal", "columns": ["a"], "value": 2.0}]
        _rf = RowFilter(_table_1)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_1, _rf.frame)

    @staticmethod
    def test_drop_if_not_equal_2():
        """
        Test that a single row is dropped.
        """
        _table_2 = DataFrame({"a": [1.0, 2.0, 2.0], "b": [3.0, 4.0, 5.0]})

        _cleanings = [{"operator": "drop_if_not_equal", "columns": ["a"], "value": 2.0}]
        _expected = DataFrame({"a": [2.0, 2.0], "b": [4.0, 5.0]})
        _rf = RowFilter(_table_2)
        _rf.filter(_cleanings)

        # TODO: This is a hack for row indexes
        _expected.index = _rf.frame.index

        assert_frame_equal(_expected, _rf.frame)

    @staticmethod
    def test_drop_if_not_equal_3():
        """
        Test that no rows are dropped even if conditions are met elsewhere.
        """
        _table_3 = DataFrame(
            {
                "a": [1.0, 2.0, 3.0, 4.0],
                "b": [5.0, 5.0, 5.0, 5.0],
                "c": [1.0, 3.0, 5.0, 7.0],
            }
        )

        _cleanings = [{"operator": "drop_if_not_equal", "columns": ["b"], "value": 5.0}]
        _rf = RowFilter(_table_3)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_3, _rf.frame)

    @staticmethod
    def test_drop_if_not_equal_4():
        """
        Test that a single row is dropped when data type is a string.
        """
        _table_4 = DataFrame({"a": ["A", "B"], "b": ["C", "D"], "c": ["E", "F"]})

        _cleanings = [{"operator": "drop_if_not_equal", "columns": ["b"], "value": "C"}]
        _expected = DataFrame({"a": ["A"], "b": ["C"], "c": ["E"]})
        _rf = RowFilter(_table_4)
        _rf.filter(_cleanings)

        # TODO: This is a hack for row indexes
        _expected.index = _rf.frame.index

        assert_frame_equal(_expected, _rf.frame)

    def test_drop_if_not_equal_5(self):
        """
        Test that an error is raised when multiple columns are passed.
        """
        _table_5 = DataFrame({"a": [3.0, 4.0, 5.0, 6.0], "b": [3.0, 7.0, 9.0, 6.0]})
        _cleanings = [
            {"operator": "drop_if_not_equal", "columns": ["a", "b"], "value": 3.0}
        ]

        _rf = RowFilter(_table_5)
        with self.assertRaises(Exception):
            _rf.filter(_cleanings)
