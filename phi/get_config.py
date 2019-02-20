# Copyright 2019 Alexander L. Hayes

"""
=============
get_config.py
=============

Read parameters from a ``config.json`` file and make these available through
a ``get_config.parameters()`` function.

Available Options
-----------------

* ``"csv_path"``: Path to directory where all ``.csv`` files are located
* ``"files"``: List of entries naming individual files

  * ``"name"``: ``.csv`` file name (``csv_path`` will be appended to the beginning)
  * ``"drop"``: [**optional**] Names of columns to drop from an individual file

* ``"target"``: Target file (what you want to predict)

  * ``"name"``: ``.csv`` file name (``csv_path`` will be appended to the beginning)
  * ``"drop"``: [**optional**] Names of columns to drop from the target file

* ``"groupings"``: List of objects describing how to aggregate columns

  * ``"operator"``: "mean", "last", or "count"
  * ``"columns"``: List of column names to apply aggregation operator to. *These columns are dropped after aggregating*
  * ``"rename"``: [**optional**] Name to apply to the new column of aggregated values

  If none is specified, the column is named according to which columns were aggregated and what operator was used

Example Usage
-------------

>>> import get_config
>>> _params = get_config.parameters(config="phi_config.json")

Example File
------------

.. code-block:: json

    {
      "csv_path": "../../Data/",
      "files": [
        {"name": "Visit1.csv", "drop": []},
        {"name": "Screening.csv"}
      ],
      "target": {
          "name": "pregnancy_outcomes.csv",
          "drop": []
      },
      "groupings": [
        {
          "operator": "mean",
          "columns": ["column1", "column2"],
          "rename": "average_1_2"
        },
        {
          "operator": "last",
          "columns": ["measure1", "measure2", "measure3"],
          "rename": "most_recent_measurement"
        }
      ]
    }
"""

import json


def parameters(config="phi_config.json"):
    """
    Read the parameters from config.
    """

    with open(config) as config_file:
        _parameters = json.load(config_file)

    # This is way too complicated for what it is doing.

    _path_list = []
    for _file in _parameters["files"]:

        # Create a path to the file for easier reading later.
        _file_path = "{0}{1}".format(_parameters["csv_path"], _file["name"])

        # Deal with potential "drop" list.
        _drop = _file["drop"] if _file.get("drop") else []

        # Append a tuple of these to the _path_list
        _path_list.append(tuple([_file_path, _drop]))

    _parameters["paths"] = _path_list

    # Similar process for the target values.
    _file_path = "{0}{1}".format(_parameters["csv_path"], _parameters["target"]["name"])
    _drop = _parameters["target"]["drop"] if _parameters["target"].get("drop") else []

    _parameters["target"] = tuple([_file_path, _drop])

    return _parameters


if __name__ == "__main__":
    raise Exception("{0} should not be ran from __main__".format(__file__))
