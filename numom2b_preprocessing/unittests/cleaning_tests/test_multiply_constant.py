# Copyright 2019 Alexander L. Hayes

"""
Test for the ``preprocess._aggregate_columns`` (multiply_constant) module.

Could use further tests with respect to:

* "Corner-Cases" of Usability:

    * Same column name provided as input multiple times
    * Constant expressed as a fraction

* Constants with data read from files.
* Constants preceded by other aggregation methods.
* Constants followed by other aggregation methods.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...clean_variables import VariableCleaner


class PreprocessMultiplyConstantTestsGeneralTests(unittest.TestCase):
    """
    Tests for the ``preprocess._aggregate_columns`` module. Assert final data frames match expectations.
    """

    @staticmethod
    def test_aggregate_multiply_constant_1():
        """Multiply a column by 1."""

        _input_table = DataFrame(
            {"ID": [0, 1, 1, 2], "a": [1, 1, 1, 1], "b": [2, 3, 4, 5]}
        )
        _groupings = [{"operator": "multiply_constant", "columns": ["a"], "value": 1}]
        _vc = VariableCleaner(_input_table)
        _vc.clean(_groupings)
        assert_frame_equal(_input_table, _vc.frame)

    @staticmethod
    def test_aggregate_multiply_constant_2():
        """Multiply a column by 2."""

        _input_table = DataFrame({"ID": [0, 1, 2], "A": [1, 2, 3], "B": [3, 2, 1]})
        _groupings = [{"operator": "multiply_constant", "columns": ["A"], "value": 2}]
        _expected = DataFrame({"ID": [0, 1, 2], "A": [2, 4, 6], "B": [3, 2, 1]})
        _vc = VariableCleaner(_input_table)
        _vc.clean(_groupings)
        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_aggregate_multiply_constant_two_columns_1():
        """Multiplying two columns by 1."""

        _input_table = DataFrame({"ID": [0, 1], "A": [1, 2], "B": [3, 4], "C": [5, 6]})
        _groupings = [
            {"operator": "multiply_constant", "columns": ["A", "B"], "value": 1}
        ]
        _vc = VariableCleaner(_input_table)
        _vc.clean(_groupings)
        assert_frame_equal(_input_table, _vc.frame)

    @staticmethod
    def test_aggregate_multiply_constant_two_columns_2():
        """Multiply two columns by a 3."""

        _input_table = DataFrame({"ID": [0, 1], "A": [1, 2], "B": [3, 4], "C": [5, 6]})
        _groupings = [
            {"operator": "multiply_constant", "columns": ["A", "B"], "value": 3.0}
        ]
        _expected = DataFrame(
            {"ID": [0, 1], "A": [3.0, 6.0], "B": [9.0, 12.0], "C": [5, 6]}
        )
        _vc = VariableCleaner(_input_table)
        _vc.clean(_groupings)
        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_aggregate_multiply_constant_two_columns_one_between():
        """Test multiplying two columns when another column exists between the two."""

        _input_table = DataFrame({"ID": [0, 1], "A": [1, 2], "B": [3, 4], "C": [5, 6]})
        _groupings = [
            {"operator": "multiply_constant", "columns": ["A", "C"], "value": 4.0}
        ]
        _expected = DataFrame(
            {"ID": [0, 1], "A": [4.0, 8.0], "B": [3, 4], "C": [20.0, 24.0]}
        )
        _vc = VariableCleaner(_input_table)
        _vc.clean(_groupings)
        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_aggregate_multiply_constant_nan_values_1():
        """Multiply a column containing NaN values by a constant."""

        _input_table = DataFrame({"ID": ["a", "b"], "A": [float("nan"), float("nan")]})
        _groupings = [{"operator": "multiply_constant", "columns": ["A"], "value": 2.0}]
        _vc = VariableCleaner(_input_table)
        _vc.clean(_groupings)
        assert_frame_equal(_input_table, _vc.frame)

    @staticmethod
    def test_aggregate_multiply_constant_nan_values_2():
        """Multiply a column containing a mix of floats and NaN values."""

        _input_table = DataFrame(
            {"ID": ["A", "B"], "A": [float("nan"), 2], "B": [2, float("nan")]}
        )
        _groupings = [
            {"operator": "multiply_constant", "columns": ["B", "A"], "value": 2.0}
        ]
        _expected = DataFrame(
            {"ID": ["A", "B"], "A": [float("nan"), 4], "B": [4, float("nan")]}
        )
        _vc = VariableCleaner(_input_table)
        _vc.clean(_groupings)
        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_aggregate_multiply_type_conversion_1():
        """Expect type conversion to succeed."""
        _input = DataFrame({"A": ["0.0", "1.0", "2.0"]})
        _expected = DataFrame({"A": [0.0, 1.0, 2.0]})
        _groupings = [{"operator": "multiply_constant", "columns": ["A"], "value": 1.0}]

        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)
        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_aggregate_multiply_type_conversion_2():
        """Expect type conversion to succeed with mix of string/float."""
        _input = DataFrame({"B": ["0.0", 1.0, "2.0"]})
        _expected = DataFrame({"B": [0.0, 1.0, 2.0]})
        _groupings = [{"operator": "multiply_constant", "columns": ["B"], "value": 1.0}]

        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)
        assert_frame_equal(_expected, _vc.frame)

    def test_aggregate_multiply_cannot_convert_1(self):
        """Test that an error is raised when type conversion fails (strings)."""
        _input = DataFrame({"A": ["a", "b", "c"]})
        _groupings = [{"operator": "multiply_constant", "columns": ["A"], "value": 1.0}]

        _vc = VariableCleaner(_input)
        with self.assertRaises(RuntimeError):
            _vc.clean(_groupings)

    def test_aggregate_multiply_cannot_convert_2(self):
        """Test taht an error is raised when type conversion fails (mix of strings and int)"""
        _input = DataFrame({"A": ["A", 1, "B"]})
        _groupings = [{"operator": "multiply_constant", "columns": ["A"], "value": 1.0}]

        _vc = VariableCleaner(_input)
        with self.assertRaises(RuntimeError):
            _vc.clean(_groupings)
