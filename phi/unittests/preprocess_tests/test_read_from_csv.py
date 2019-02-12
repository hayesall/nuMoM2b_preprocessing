# Copyright 2019 Alexander L. Hayes

"""
Test for the preprocess module.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
from numpy import float64
import unittest

# Tests for:
from ... import preprocess


class ReadTargetTest(unittest.TestCase):
    """
    Tests for the ``preprocess._build_target_table`` module. Assert target csv files load with valid parameters.
    """

    @staticmethod
    def test_reading_from_target1_csv_1():
        """
        Test ``target1.csv`` while dropping ``column1`` and ``column2``.
        """

        _parameters = {
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["column1", "column2"],
            )
        }

        _name, _drop = _parameters["target"][0], _parameters["target"][1]

        _target = preprocess._build_target_table(_name, _drop)
        _expected = DataFrame(
            {"PublicID": ["A1", "B2", "B4"], "target_variable": [0, 0, 1]}
        )

        assert_frame_equal(_expected, _target)

    @staticmethod
    def test_reading_from_target1_csv_2():
        """
        Test ``target1.csv`` dropping ``column1``.
        """

        _parameters = {
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["column1"],
            )
        }

        _name, _drop = _parameters["target"][0], _parameters["target"][1]

        _target = preprocess._build_target_table(_name, _drop)
        _expected = DataFrame(
            {
                "PublicID": ["A1", "B2", "B4"],
                "column2": [23, 11, 11],
                "target_variable": [0, 0, 1],
            }
        )

        assert_frame_equal(_expected, _target)

    @staticmethod
    def test_reading_from_target1_csv_3():
        """
        Test ``target1.csv`` dropping ``column2``.
        """

        _parameters = {
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["column2"],
            )
        }

        _name, _drop = _parameters["target"][0], _parameters["target"][1]

        _target = preprocess._build_target_table(_name, _drop)
        _expected = DataFrame(
            {
                "PublicID": ["A1", "B2", "B4"],
                "column1": [25, 24, 20],
                "target_variable": [0, 0, 1],
            }
        )

        assert_frame_equal(_expected, _target)


class ReadCSVTest(unittest.TestCase):
    """
    Tests for ``preprocess._build_table``.
    """

    @staticmethod
    def test_target1_and_csv1_1():
        """
        Join ``target1.csv`` and ``csv1.csv``
        """

        _parameters = {
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["column1", "column2"],
            ),
            "paths": [
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv1.csv",
                    ["column1", "column2", "column3", "column4"],
                )
            ],
        }

        _table = preprocess._build_table(_parameters)
        _expected = DataFrame(
            {
                "PublicID": ["A1", "B2", "B4"],
                "target_variable": [0, 0, 1],
                "column5": [float64("nan"), float64("nan"), 5.0],
            }
        )

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_target1_and_csv1_2():
        """
        Join ``target1.csv`` and ``csv1.csv``
        """

        _parameters = {
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["column2"],
            ),
            "paths": [
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv1.csv",
                    ["column1", "column2"],
                )
            ],
        }

        _table = preprocess._build_table(_parameters)
        _expected = DataFrame(
            {
                "PublicID": ["A1", "B2", "B4"],
                "column1": [25, 24, 20],
                "target_variable": [0, 0, 1],
                "column3": [1, 2, 3],
                "column4": [float64("nan"), 3.0, 4.0],
                "column5": [float64("nan"), float64("nan"), 5.0],
            }
        )

        assert_frame_equal(_expected, _table)

    @staticmethod
    def test_target1_csv1_and_csv2_1():
        """
        Join ``target1.csv``, ``csv1.csv``, and ``csv2.csv``. Maintain one column from each.
        """

        _parameters = {
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["column2"],
            ),
            "paths": [
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv1.csv",
                    ["column1", "column3", "column4", "column5"],
                ),
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv2.csv",
                    ["column1", "column2", "column4", "column5"],
                ),
            ],
        }

        _table = preprocess._build_table(_parameters)
        _expected = DataFrame(
            {
                "PublicID": ["A1", "B2", "B4"],
                "column1": [25, 24, 20],
                "target_variable": [0, 0, 1],
                "column2": [3, 2, 1],
                "column3": [1, 2, 3],
            }
        )

        assert_frame_equal(_expected, _table)
