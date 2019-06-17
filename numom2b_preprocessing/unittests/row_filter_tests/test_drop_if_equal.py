# Copyright © 2019 Alexander L. Hayes

"""
Tests for the variable/column cleaning with variable dropping on equality.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...row_filter import RowFilter


class CleanDropIfEqualTests(unittest.TestCase):
    """
    Tests for the ``preprocess._clean_variables`` module dropping rows based on "=="
    """

    @staticmethod
    def test_drop_if_equal_1():
        """
        Test that no rows are dropped if equality conditions are not met.
        """
        _table_1 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 3.0, 4.0]})

        _cleanings = [{"operator": "drop_if_equal", "columns": ["a"], "value": 5.0}]
        _rf = RowFilter(_table_1)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_1, _rf.frame)

    @staticmethod
    def test_drop_if_equal_2():
        """
        Test that a single row is dropped
        """
        _table_2 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 3.0, 4.0]})

        _cleanings = [{"operator": "drop_if_equal", "columns": ["a"], "value": 1.0}]
        _expected = DataFrame({"a": [2.0, 3.0], "b": [3.0, 4.0]})

        _rf = RowFilter(_table_2)
        _rf.filter(_cleanings)

        # TODO: There might be a bug in how pandas checks indexes, this is a hack:
        _expected.index = _rf.frame.index

        assert_frame_equal(_expected, _rf.frame)

    @staticmethod
    def test_drop_if_equal_3():
        """
        Test that no rows are dropped even if conditions would be met in a different row.
        """
        _table_3 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 3.0, 4.0]})

        _cleanings = [{"operator": "drop_if_equal", "columns": ["b"], "value": 1.0}]

        _rf = RowFilter(_table_3)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_3, _rf.frame)

    @staticmethod
    def test_drop_if_equal_4():
        """
        Test that a single row is dropped when data type is a string.
        """
        _table_4 = DataFrame({"a": ["A", "B"], "b": ["C", "D"], "c": ["E", "F"]})

        _cleanings = [{"operator": "drop_if_equal", "columns": ["a"], "value": "B"}]
        _expected = DataFrame({"a": ["A"], "b": ["C"], "c": ["E"]})

        _rf = RowFilter(_table_4)
        _rf.filter(_cleanings)

        # TODO: This is a hack for row indexes
        _expected.index = _rf.frame.index

        assert_frame_equal(_expected, _rf.frame)

    @staticmethod
    def test_drop_if_equal_5():
        """
        Test that everything is dropped.
        """
        _table_5 = DataFrame(
            {
                "a": [3.0, 3.0, 3.0, 3.0],
                "b": [4.5, 4.5, 1.1, 2.2],
                "c": [1.0, 2.0, 3.0, 4.0],
            }
        )

        _cleanings = [{"operator": "drop_if_equal", "columns": ["a"], "value": 3.0}]
        _expected = DataFrame({"a": [], "b": [], "c": []})

        _rf = RowFilter(_table_5)
        _rf.filter(_cleanings)
        assert_frame_equal(_expected, _rf.frame)

    def test_drop_if_equal_6(self):
        """
        Test that an error is raised when multiple columns are passed.
        """
        _table_6 = DataFrame({"a": [3.0, 4.0, 5.0, 6.0], "b": [3.0, 7.0, 9.0, 6.0]})
        _cleanings = [
            {"operator": "drop_if_equal", "columns": ["a", "b"], "value": 3.0}
        ]

        with self.assertRaises(Exception):
            _rf = RowFilter(_table_6)
            _rf.filter(_cleanings)
