# Copyright © 2019 Alexander L. Hayes

"""
Tests for the variable/column cleaning with variable dropping on ">"
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...row_filter import RowFilter


class CleanDropIfGreaterThan(unittest.TestCase):
    """
    Tests for the ``preprocess._clean_variables`` module dropping rows on ">"
    """

    @staticmethod
    def test_drop_if_greater_than_1():
        """
        Test that no rows are dropped if conditions are not met.
        """
        _table_1 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 3.0, 4.0]})

        _cleanings = [{"operator": "drop_if_greater", "columns": ["a"], "value": 10.0}]
        _rf = RowFilter(_table_1)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_1, _rf.frame)

    @staticmethod
    def test_drop_if_greater_than_2():
        """
        Test that a single row is dropped.
        """
        _table_2 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 3.0, 4.0]})

        _cleanings = [{"operator": "drop_if_greater", "columns": ["a"], "value": 2.0}]
        _expected = DataFrame({"a": [1.0, 2.0], "b": [2.0, 3.0]})
        _rf = RowFilter(_table_2)
        _rf.filter(_cleanings)

        # TODO: There might be a bug in how pandas checks indexes, this is a hack:
        _expected.index = _rf.frame.index

        assert_frame_equal(_expected, _rf.frame)

    @staticmethod
    def test_drop_if_greater_than_3():
        """
        Test test that no rows are dropped even if conditions are met in a different row.
        """
        _table_3 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 3.0, 4.0]})

        _cleanings = [{"operator": "drop_if_greater", "columns": ["a"], "value": 3.0}]
        _rf = RowFilter(_table_3)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_3, _rf.frame)

    @staticmethod
    def test_drop_if_greater_than_4():
        """
        Test that everything is dropped.
        """
        _table_4 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 3.0, 4.0]})

        _cleanings = [{"operator": "drop_if_greater", "columns": ["a"], "value": 0.0}]
        _expected = DataFrame({"a": [], "b": []})

        _rf = RowFilter(_table_4)
        _rf.filter(_cleanings)

        assert_frame_equal(_expected, _rf.frame)

    def test_drop_if_greater_than_5(self):
        """
        Test that an error is raised when multiple columns are passed.
        """
        _table_5 = DataFrame({"a": [3.0, 4.0, 5.0, 6.0], "b": [3.0, 7.0, 9.0, 6.0]})
        _cleanings = [
            {"operator": "drop_if_greater", "columns": ["a", "b"], "value": 3.0}
        ]

        with self.assertRaises(Exception):
            _rf = RowFilter(_table_5)
            _rf.filter(_cleanings)
