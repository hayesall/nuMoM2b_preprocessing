============
Architecture
============

The architecture of ``nuMoM2b_preprocessing`` is intended to be fairly simple, having
one component for **parsing configuration options** and another for performing the
**aggregations and joins** on the contents of the data.

The main source of complexity is therefore in writing the configuration files. However,
these can be fairly consistent, and can be shared.

Input:

1. Configuration File
2. nuMoM2b data base

Output:

1. ``data.csv`` contains a single table
2. ``debug.log`` (Optional) contains a log of all operations performed

.. image:: _static/img/nuMoM2b_preprocessing_architecture.png
   :alt: nuMoM2b_preprocessing architecture.
