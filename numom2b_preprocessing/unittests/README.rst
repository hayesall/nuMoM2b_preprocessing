##################################
numom2b_preprocessing Unit Testing
##################################

First-time setup:

.. code-block:: bash

    pip install -r numom2b_preprocessing/unittests/requirements.txt

Unit tests and code coverage are handled through ``coverage`` and ``unittest``:

.. code-block:: bash

    coverage run numom2b_preprocessing/unittests/test.py
    coverage html
    open -a "Firefox" htmlcov/index.html

