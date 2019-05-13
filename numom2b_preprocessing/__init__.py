# Copyright 2019 Alexander L. Hayes

"""
===
phi
===

A Python package for the Precision Health Initiative and analysis of *nuMoM2b* Data.

Project documentation
---------------------

Most documentation is provided as part of the source, but may also be accessed by
building a copy with Sphinx.

Using ``phi``
-------------

The package may be used as is, or may be installed.

Since the package is in the early stages, it's recommended to do a ``develop`` install.

.. code-block:: bash

    python setup.py develop

Once installed, the package may be used on its own or incorporated into other scripts or pipelines.

>>> import phi
>>> print(phi.__version__)

Submodules
----------

No submodules are imported by default.

* ``phi.get_config``
* ``phi.preprocess``

``phi.get_config``
------------------

>>> from phi import get_config
>>> PARAMETERS = get_config.parameters("phi_config.json")

``phi.preprocess``
------------------

``phi.preprocess`` should currently be used in tandem with the ``get_config`` module.

>>> from phi import get_config
>>> from phi import preprocess
>>> PARAMETERS = get_config.parameters("phi_config.json")
>>> df = preprocess.run(PARAMETERS)
"""

__author__ = "Alexander L. Hayes (@batflyer)"
__copyright__ = "Copyright 2019 Alexander L. Hayes"
__license__ = "Not-Declared"

__version__ = "0.0.1"
__status__ = "Alpha"
__maintainer__ = "Alexander L. Hayes (@batflyer)"
__email__ = "hayesall@iu.edu"

__credits__ = ["Alexander L. Hayes (@batflyer)", "Rafael Guerrero (@guerreror)"]
