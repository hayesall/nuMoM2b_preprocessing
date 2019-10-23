# Copyright © 2019 Alexander L. Hayes

"""
Tests for the variable/column with cleaning with ``RowFilter._equal(columns, "NaN")``
"""

from numpy import nan
from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...row_filter import RowFilter


class CleanDropIfNaNTests(unittest.TestCase):
    """
    Tests for the ``preprocess._clean_variables`` module dropping rows based on ``== "NaN"``
    """

    @staticmethod
    def test_drop_if_equal_nan_1():
        """Test that nothing is dropped"""
        _table_1 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 3.0, 4.0]})

        _cleanings = [
            {"operator": "drop_if_equal", "columns": ["a"], "value": "NaN"},
            {"operator": "drop_if_equal", "columns": ["b"], "value": "NaN"},
        ]
        _rf = RowFilter(_table_1)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_1, _rf.frame)

    @staticmethod
    def test_drop_if_equal_nan_2():
        """Test that a single row is dropped"""
        _table_2 = DataFrame({"a": [1.0, nan, 3.0], "b": [2.0, 3.0, 4.0]})

        _cleanings = [{"operator": "drop_if_equal", "columns": ["a"], "value": "NaN"}]
        _expected = DataFrame({"a": [1.0, 3.0], "b": [2.0, 4.0]})

        _rf = RowFilter(_table_2)
        _rf.filter(_cleanings)

        # TODO(@hayesall): This is a hack for indexes
        _expected.index = _rf.frame.index

        assert_frame_equal(_expected, _rf.frame)

    @staticmethod
    def test_drop_if_equal_nan_3():
        """Test that everything is dropped."""
        _table_3 = DataFrame({"a": [nan, nan, nan], "b": [1.0, 2.0, 3.0]})

        _cleanings = [{"operator": "drop_if_equal", "columns": ["a"], "value": "NaN"}]
        _expected = DataFrame({"a": [], "b": []})

        _rf = RowFilter(_table_3)
        _rf.filter(_cleanings)

        assert_frame_equal(_expected, _rf.frame)

    def test_drop_if_equal_nan_4(self):
        """Test that an error is raised when multiple columns are passed."""
        _table_4 = DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 3.0, 4.0]})
        _cleanings = [{"operator": "drop_if_equal", "columns": ["a", "b"], "value": "NaN"}]

        with self.assertRaises(Exception):
            _rf = RowFilter(_table_4)
            _rf.filter(_cleanings)

    @staticmethod
    def test_drop_if_equal_nan_5():
        """Test that nothing is dropped when the condition is passed in another row."""
        _table_5 = DataFrame({"a": [nan, nan, nan], "b": [1.0, 2.0, 3.0]})
        _cleanings = [{"operator": "drop_if_equal", "columns": ["b"], "value": "NaN"}]

        _rf = RowFilter(_table_5)
        _rf.filter(_cleanings)

        assert_frame_equal(_table_5, _rf.frame)
