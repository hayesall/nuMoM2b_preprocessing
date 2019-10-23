##############
``get_config``
##############

.. automodule:: numom2b_preprocessing.get_config
    :members:
    :undoc-members:
    :show-inheritance:

Available Options
=================

* ``"csv_path"``: Path to directory where all ``.csv`` files are located
* ``"files"``: List of entries naming individual files

  * ``"name"``: ``.csv`` file name (``csv_path`` will be appended to the beginning)
  * ``"variables"``: Names of columns to include from an individual file

* ``"target"``: Target file (what you want to predict)

  * ``"name"``: ``.csv`` file name (``csv_path`` will be appended to the beginning)
  * ``"variables"``: Names of columns to include from the target file

* ``"aggregate_columns"``: List of objects describing how to aggregate columns

  * ``"operator"``: "mean", "last", or "count"
  * ``"columns"``: List of column names to apply aggregation operator to. *These columns are dropped after aggregating*
  * ``"rename"``: [**optional**] Name to apply to the new column of aggregated values

  If none is specified, the column is named according to which columns were aggregated and what operator was used

Example Usage
=============

>>> from numom2b_preprocessing import get_config
>>> _params = get_config.parameters(config="phi_config.json")

Example File
============

.. code-block:: json

    {
      "comments": [
        "Screening questions asked during visit 1.",
        "These are primarily yes/no questions.",
      ],
      "log_file": "nuMoM2b_screening_questions.log",
      "csv_path": "~/Desktop/PrecisionHealth/Data/numom_data/",
      "target": {
        "name": "Ancillary/Pregnancy_outcomes.csv",
        "variables": ["PublicID", "oDM"]
      },
      "files": [
        {
          "name": "Screening_Admin_Visits/Visit1.csv",
          "variables": [
            "PublicID", "V1AD03", "V1AD05", "V1AD17", "V1AD18", "V1AF01",
            "V1AF03", "V1AF03a1", "V1AF03a2", "V1AF03a3", "V1AF03a4",
            "V1AF03b", "V1AF03c", "V1AF04", "V1AF14", "V1AG01", "V1AG02",
            "V1AG03", "V1AI01"
          ]
        }
      ],
      "aggregate_columns": []
    }
