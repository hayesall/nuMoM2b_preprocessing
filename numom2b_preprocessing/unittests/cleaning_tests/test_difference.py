# Copyright © 2019 Alexander L. Hayes

"""
Test for the ``preprocess._aggregate_columns._difference`` module.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...clean_variables import VariableCleaner


class PreprocessConstantDifferenceTests(unittest.TestCase):
    """
    Tests for the ``preprocess._aggregate_columns._difference`` module. Assert final data frames match expectations.
    """

    @staticmethod
    def test_clean_difference_ints_0():
        """Test subtracting 0 from a column."""
        _input = DataFrame({"A": [1, 2, 3]})
        _expected = DataFrame({"A": [1, 2, 3]})

        _groupings = [{"operator": "difference", "columns": ["A"], "value": 0}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_clean_difference_ints_1():
        """Test subtracting 1 from a column."""
        _input = DataFrame({"A": [1, 2, 3]})
        _expected = DataFrame({"A": [0, 1, 2]})

        _groupings = [{"operator": "difference", "columns": ["A"], "value": 1}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_clean_difference_floats_0():
        """Test subtracting 0.0 from a column."""
        _input = DataFrame({"A": [1.0, 2.0, 3.0]})
        _expected = DataFrame({"A": [1.0, 2.0, 3.0]})

        _groupings = [{"operator": "difference", "columns": ["A"], "value": 0.0}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_clean_difference_floats_negative_1():
        """Test subtracting -1.0 from a column."""
        _input = DataFrame({"A": [1.0, 2.0, 3.0]})
        _expected = DataFrame({"A": [2.0, 3.0, 4.0]})

        _groupings = [{"operator": "difference", "columns": ["A"], "value": -1.0}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)


class PreprocessVariableDifferenceTests(unittest.TestCase):
    """
    Tests for the ``preprocess._aggregate_columns._difference`` module with column subtraction.
    """

    @staticmethod
    def test_clean_difference_int_column():
        """Test subtracting the right column from the left."""
        _input = DataFrame({"A": [1, 2, 3], "B": [2, 3, 4]})
        _expected = DataFrame({"A": [-1, -1, -1], "B": [2, 3, 4]})

        _groupings = [{"operator": "difference", "columns": ["A"], "value": "B"}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_clean_difference_right_string_column():
        """Test subtracting the right column from the left. Right column has strings."""
        _input = DataFrame({"A": [1, 2, 3], "B": ["2", "3", "4"]})
        _expected = DataFrame({"A": [-1.0, -1.0, -1.0], "B": ["2", "3", "4"]})

        _groupings = [{"operator": "difference", "columns": ["A"], "value": "B"}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_clean_difference_left_string_column():
        """Test subtracting the right column from the left. Left column has strings."""
        _input = DataFrame({"A": ["1", "2", "3"], "B": [2, 3, 4]})
        _expected = DataFrame({"A": [-1.0, -1.0, -1.0], "B": [2, 3, 4]})

        _groupings = [{"operator": "difference", "columns": ["A"], "value": "B"}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_clean_difference_both_string_column():
        """Test subtracting the right column from the left. Both left and right have strings."""
        _input = DataFrame({"A": ["1", "2", "3"], "B": ["2", "3", "4"]})
        _expected = DataFrame({"A": [-1.0, -1.0, -1.0], "B": ["2", "3", "4"]})

        _groupings = [{"operator": "difference", "columns": ["A"], "value": "B"}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)

    def test_clean_ambiguous_difference(self):
        """Test that a ValueError is raised when subtracting multiple named columns."""
        _input = DataFrame({"a": [1, 2], "b": [2, 3], "c": [3, 4]})
        _groupings = [{"operator": "difference", "columns": ["a", "b"], "value": "c"}]

        _vc = VariableCleaner(_input)
        with self.assertRaises(ValueError):
            _vc.clean(_groupings)

    def test_clean_difference_cannot_convert(self):
        """Test that a RuntimeError is raised when columns cannot be converted to floats."""
        _input = DataFrame({"a": [1, "b"], "b": [1, "c"]})
        _groupings = [{"operator": "difference", "columns": ["a"], "value": "b"}]

        _vc = VariableCleaner(_input)
        with self.assertRaises(RuntimeError):
            _vc.clean(_groupings)
