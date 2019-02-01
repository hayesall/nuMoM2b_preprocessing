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
        "Visit1.csv",
        "Screening.csv"
      ],
      "target": "pregnancy_outcomes.csv"
    }

"""

import json


def parameters(config="phi_config.json"):
    """
    Read the parameters from config.
    """

    with open(config) as config_file:
        _parameters = json.load(config_file)

    _path_list = []
    for _file in _parameters["files"]:
        _path_list.append("{0}{1}".format(_parameters["csv_path"], _file))

    _parameters["paths"] = _path_list

    return _parameters


if __name__ == "__main__":
    raise Exception("{0} should not be ran from __main__".format(__file__))
