# Copyright 2019 Alexander L. Hayes

"""
Read parameters from a ``config.json`` file and make these available through
a ``get_config.parameters()`` function.
"""

import json


def parameters(config="phi_config.json"):
    """
    Read the parameters from a configuration file.

    :arg config: JSON configuration path/file_name.json
    :type config: str
    :return: dict
    """

    with open(config) as config_file:
        _parameters = json.load(config_file)

    # TODO: This could be simplified. Refactor where commented.
    _path_list = []
    for _file in _parameters["files"]:

        # Create a path to the file for easier reading later.
        _file_path = "{0}{1}".format(_parameters["csv_path"], _file["name"])

        # Deal with the potential "variables" list
        _variables = _file["variables"] if _file.get("variables") else []

        # Append a tuple of these to the _path_list
        _path_list.append(tuple([_file_path, _variables]))

    _parameters["paths"] = _path_list

    # Similar process for the target values.
    _file_path = "{0}{1}".format(_parameters["csv_path"], _parameters["target"]["name"])
    _variables = (
        _parameters["target"]["variables"]
        if _parameters["target"].get("variables")
        else []
    )

    _parameters["target"] = tuple([_file_path, _variables])

    return _parameters


if __name__ == "__main__":
    raise Exception("{0} should not be ran from __main__".format(__file__))
