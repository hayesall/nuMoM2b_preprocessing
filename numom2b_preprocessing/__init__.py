# Copyright 2019 Alexander L. Hayes

"""
:meth:`numom2b_preprocessing.get_config.parameters`
---------------------------------------------------

Read a configuration file and parse the parameters.

>>> import numom2b_preprocessing
>>> PARAMETERS = numom2b_preprocessing.parameters("phi_config.json")

:meth:`numom2b_preprocessing.preprocess.run`
--------------------------------------------

Use the configuration parameters to manipulate the data.

This should generally be used in tandem with the ``get_config`` module.

>>> import numom2b_preprocessing
>>> PARAMETERS = numom2b_preprocessing.parameters("phi_config.json")
>>> df = numom2b_preprocessing.run(PARAMETERS)
"""

from ._meta import (
    __author__,
    __copyright__,
    __license__,
    __version__,
    __status__,
    __maintainer__,
    __email__,
    __credits__,
)
from .get_config import parameters
from .preprocess import run
