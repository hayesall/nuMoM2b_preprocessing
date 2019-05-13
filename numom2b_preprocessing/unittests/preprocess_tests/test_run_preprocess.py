# Copyright 2019 Alexander L. Hayes

"""
Test for the preprocess.run module.

Generally these will be aimed at testing the first part of the pipeline: reading from a configuration file,
reading `.csv` files based on configuration settings, then aggregating over a set of columns.
"""

from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
from numpy import float64
import unittest

# Tests for:
from ... import preprocess
from ... import get_config


class RunPreprocessingTest(unittest.TestCase):
    """
    Tests for the ``preprocess.run`` module. Assert that the created DataFrame matches expectations.
    """

    @staticmethod
    def test_run_preprocessing_with_config_3():
        """
        Test whether ``preprocess.run`` aggregates correctly when using ``config3.json``
        """

        _parameters = get_config.parameters(
            "numom2b_preprocessing/unittests/config_tests/sample_config_files/config3.json"
        )

        _expected = DataFrame(
            {
                "PublicID": ["A1", "B2", "B4"],
                "target_variable": [0, 0, 1],
                "last345": ["a", "b", "c"],
                "meancolumn1column2": [2.0, 2.0, 2.0],
            }
        )

        _target = preprocess.run(_parameters)

        assert_frame_equal(_expected, _target)

    @staticmethod
    def test_run_preprocessing_with_config2():
        """
        Simpler config file with no aggregation performed.

        Since there are duplicate column names, this will also create a DataFrame with ``_x`` and ``_y`` appended.
        """

        _parameters = get_config.parameters(
            "numom2b_preprocessing/unittests/config_tests/sample_config_files/config2.json"
        )

        _expected = DataFrame(
            {
                "PublicID": ["A1", "B2", "B4"],
                "target_variable": [0, 0, 1],
                "column4_x": [float64("nan"), 3.0, 4.0],
                "column5_x": [float64("nan"), float64("nan"), 5.0],
                "column3": [1, 2, 3],
                "column4_y": [2.0, 3.0, float64("nan")],
                "column5_y": ["a", "b", "c"],
                "column2": [1, 1, 4],
            }
        )

        _target = preprocess.run(_parameters)
        assert_frame_equal(_expected, _target)
