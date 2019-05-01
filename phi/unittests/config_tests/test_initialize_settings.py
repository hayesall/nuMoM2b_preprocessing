# Copyright 2019 Alexander L. Hayes

"""
Test for the get_config module.

Historical Notes
----------------

The expected contents of the configuration files has changed as this project has evolved over time——therefore these
tests somewhat represent these changes.
"""

import unittest

# Tests for:
from ... import get_config


class InitializeConfigurationTest(unittest.TestCase):
    """
    Initialize loading from config files with (possibly) ideal settings: good
    formatting, correct path variables, etc.
    """

    def test_initialize_configuration_1(self):
        """
        Test contents of ``config_tests/sample_config_files/config1.json``.
        """

        _expected = {
            "csv_path": "phi/unittests/config_tests/sample_config_files/",
            "files": [{"name": "csv1.csv"}, {"name": "csv2.csv"}],
            "target": (
                "phi/unittests/config_tests/sample_config_files/target1.csv",
                [],
            ),
            "paths": [
                ("phi/unittests/config_tests/sample_config_files/csv1.csv", []),
                ("phi/unittests/config_tests/sample_config_files/csv2.csv", []),
            ],
        }
        _params = get_config.parameters(
            config="phi/unittests/config_tests/sample_config_files/config1.json"
        )

        self.assertEqual(_params, _expected)

    def test_initialize_configuration_2(self):
        """
        Test contents of ``config_tests/sample_config_files/config2.json``

        This contains "drop" directives.
        """

        _expected = {
            "csv_path": "phi/unittests/preprocess_tests/sample_csv_files/",
            "files": [
                {
                    "name": "csv1.csv",
                    "variables": ["PublicID", "column4", "column5", "column3"],
                },
                {
                    "name": "csv2.csv",
                    "variables": ["PublicID", "column4", "column5", "column2"],
                },
            ],
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["PublicID", "target_variable"],
            ),
            "paths": [
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv1.csv",
                    ["PublicID", "column4", "column5", "column3"],
                ),
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv2.csv",
                    ["PublicID", "column4", "column5", "column2"],
                ),
            ],
        }
        _params = get_config.parameters(
            config="phi/unittests/config_tests/sample_config_files/config2.json"
        )

        self.assertEqual(_params, _expected)

    def test_initialize_configuration_3(self):
        """
        Test contents of ``config_tests/sample_config_files/config3.json``

        :return: None
        """

        _expected = {
            "csv_path": "phi/unittests/preprocess_tests/sample_csv_files/",
            "files": [
                {"name": "csv1.csv", "variables": ["PublicID", "column1", "column2"]},
                {
                    "name": "csv2.csv",
                    "variables": ["PublicID", "column3", "column4", "column5"],
                },
            ],
            "target": (
                "phi/unittests/preprocess_tests/sample_csv_files/target1.csv",
                ["PublicID", "target_variable"],
            ),
            "paths": [
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv1.csv",
                    ["PublicID", "column1", "column2"],
                ),
                (
                    "phi/unittests/preprocess_tests/sample_csv_files/csv2.csv",
                    ["PublicID", "column3", "column4", "column5"],
                ),
            ],
            "groupings": [
                {
                    "operator": "last",
                    "columns": ["column3", "column4", "column5"],
                    "rename": "last345",
                },
                {"operator": "mean", "columns": ["column1", "column2"]},
            ],
        }

        _params = get_config.parameters(
            config="phi/unittests/config_tests/sample_config_files/config3.json"
        )

        self.assertEqual(_params, _expected)
