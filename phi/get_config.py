# Copyright 2019 Alexander L. Hayes

"""
=============
get_config.py
=============

Read parameters from the ``config.json`` file and make these available through
a ``get_config.parameters`` variable.

Provides the ``get_config.parameters()`` function.

Available Options
-----------------

* ``data_path``:
* ``files``
* ``target``

Example Usage
-------------

.. code-block:: python

    import get_config

    _params = get_config.parameters(config="phi_config.json")

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
