import unittest
import os
from sys import exit

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('tests', pattern='*.py', top_level_dir='.')
    result = unittest.TextTestRunner().run(all_tests)
    if len(result.errors) != 0 or len(result.failures) != 0:
        exit(1)
