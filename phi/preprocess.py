# Copyright 2019 Alexander L. Hayes

"""
================
preprocessing.py
================

A script for aligning the columns of the Gestational Diabetes data.

Assumes that a Data folder exists.
"""

# Local imports
import get_config

# Package imports
import pandas as pd

if __name__ == "__main__":

    _data_paths = get_config.parameters["paths"]

    for _csv in _data_paths:
        pd.read_csv(_csv)
