# Copyright 2019 Alexander L. Hayes

"""
==========
Unit Tests
==========

Unit test runner for PHI software.
"""

import argparse
import unittest

if __name__ == "__main__":

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("-v", "--verbose", default=1, type=int)
    ARGS = PARSER.parse_args()

    TESTSUITE = unittest.TestLoader().discover(".")
    RUNNER = unittest.TextTestRunner(verbosity=ARGS.verbose)

    RESULTS = RUNNER.run(TESTSUITE)
    if RESULTS.failures or RESULTS.errors:
        raise Exception("Encountered errors during runner.run")
