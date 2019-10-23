# Copyright © 2019 Alexander L. Hayes

"""
Test for the ``preprocess._aggregate_columns._replace`` module.
"""

from numpy import nan
from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
import unittest

# Tests for:
from ...clean_variables import VariableCleaner


class CleanReplaceTests(unittest.TestCase):

    @staticmethod
    def test_clean_replace_string_values():
        """Replace strings in a column."""
        _input = DataFrame({"a": [0, 1, "b"]})
        _expected = DataFrame({"a": [0, 1, 2]})

        _groupings = [{"operator": "replace", "columns": ["a"], "value": ["b", 2]}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_clean_replace_int_values():
        """Replace an int in a column."""
        _input = DataFrame({"a": [0, 1, "b"]})
        _expected = DataFrame({"a": [2, 1, "b"]})

        _groupings = [{"operator": "replace", "columns": ["a"], "value": [0, 2]}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)

    @staticmethod
    def test_clean_replace_nan_values():
        """Replace NaN values in a column."""
        _input = DataFrame({"a": [0.0, 1.0, "a"]})
        _expected = DataFrame({"a": [0.0, 1.0, nan]})

        _groupings = [{"operator": "replace", "columns": ["a"], "value": ["a", "NaN"]}]
        _vc = VariableCleaner(_input)
        _vc.clean(_groupings)

        assert_frame_equal(_expected, _vc.frame)
