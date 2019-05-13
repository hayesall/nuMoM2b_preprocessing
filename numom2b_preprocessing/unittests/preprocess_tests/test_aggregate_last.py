# Copyright 2019 Alexander L. Hayes

"""
Test for the ``preprocess._aggregate_columns`` (last) module.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
from numpy import float64
import unittest

# Tests for:
from ... import preprocess


class PreprocessLastTests(unittest.TestCase):
    """
    Tests for the ``preprocess._aggregate_columns`` module. Assert final data frames match expectations.
    """

    @staticmethod
    def test_aggregate_last_columns_1():
        """
        Test aggregating with the "last" operation on an example DataFrame.
        """

        _input_table = DataFrame(
            {
                "ID": [0, 1, 1, 2],
                "a": [float64("nan"), float64("nan"), float64("nan"), float64("nan")],
                "b": [2, 3, 4, 5],
            }
        )
        _groupings = [{"operator": "last", "columns": ["a", "b"]}]
        _expected = DataFrame({"ID": [0, 1, 1, 2], "lastab": [2.0, 3.0, 4.0, 5.0]})

        _table = preprocess._aggregate_columns(_input_table, _groupings)

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_aggregate_last_columns2():
        """
        Test aggregating with the "last" operation on an example DataFrame with a mix of float64("nan") values.
        """

        _input_table = DataFrame(
            {
                "ID": [1.0, -9.2, 6.4, 7.4],
                "a": [1.0, 2.0, float64("nan"), float64("nan")],
                "b": [float64("nan"), float64("nan"), float64("nan"), 2.0],
            }
        )
        _groupings = [{"operator": "last", "columns": ["a", "b"], "rename": "c"}]
        _expected = DataFrame(
            {"ID": [1.0, -9.2, 6.4, 7.4], "c": [1.0, 2.0, float64("nan"), 2.0]}
        )

        _table = preprocess._aggregate_columns(_input_table, _groupings)

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_aggregate_last_columns3():
        """
        Test aggregating with the "last" operation on only float64("nan") values.
        """
        _input_table = DataFrame(
            {
                "ID": ["a", "b"],
                "a": [float64("nan"), float64("nan")],
                "b": [float64("nan"), float64("nan")],
            }
        )
        _groupings = [{"operator": "last", "columns": ["a", "b"], "rename": "="}]
        _expected = DataFrame({"ID": ["a", "b"], "=": [float64("nan"), float64("nan")]})
        _table = preprocess._aggregate_columns(_input_table, _groupings)
        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_target1_csv1_csv2_aggregate_last():
        """
        Join ``target1.csv``, ``csv1.csv``, and ``csv2.csv``. Maintain one column from each.
        Aggregate the new ``column2`` and ``column3`` using the "last" operation.

        There are no ``NaN`` values in ``column3``, so the result should be equal to ``column3`` while dropping 2.
        """

        _parameters = {
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["PublicID", "column1", "target_variable"],
            ),
            "paths": [
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv1.csv",
                    ["PublicID", "column3"],
                ),
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv2.csv",
                    ["PublicID", "column2"],
                ),
            ],
            "groupings": [
                {
                    "operator": "last",
                    "columns": ["column2", "column3"],
                    "rename": "last23",
                }
            ],
        }

        _table = preprocess._build_table(_parameters)
        _table = preprocess._aggregate_columns(_table, _parameters["groupings"])

        _expected = DataFrame(
            {
                "PublicID": ["A1", "B2", "B4"],
                "column1": [25, 24, 20],
                "target_variable": [0, 0, 1],
                "last23": [1, 2, 3],
            }
        )

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_target1_csv1_csv2_aggregate_last_columns():
        """
        """

        _parameters = {
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["PublicID", "target_variable"],
            ),
            "paths": [
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv1.csv",
                    ["PublicID", "column3", "column4", "column5"],
                )
            ],
            "groupings": [
                {"operator": "last", "columns": ["column3", "column4", "column5"]}
            ],
        }

        _table = preprocess._build_table(_parameters)
        _table = preprocess._aggregate_columns(_table, _parameters["groupings"])

        _expected = DataFrame(
            {
                "PublicID": ["A1", "B2", "B4"],
                "target_variable": [0, 0, 1],
                "lastcolumn3column4column5": [1.0, 3.0, 5.0],
            }
        )

        assert_frame_equal(_expected, _table)
