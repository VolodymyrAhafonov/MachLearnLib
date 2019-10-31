import unittest

from utils.data.preparation.data_cleaner.MeanDataCleaner import MeanDataCleaner
from utils.data.preparation.data_cleaner.BaseDataCleaner import HOLE_SYMBOLS


class test_MeanDataCleaner(unittest.TestCase):
    def test_MeanpDataCleaner_clean_data(self):
        list_to_clean = [['1', '2', '3'],
                         [HOLE_SYMBOLS[0], HOLE_SYMBOLS[0], '4'],
                         [HOLE_SYMBOLS[2], '6', '7'],
                         [HOLE_SYMBOLS[0], HOLE_SYMBOLS[2], '6'],
                         [HOLE_SYMBOLS[1], '11', '12'],
                         [HOLE_SYMBOLS[2], '13', '0']]

        expected_list_after_clean = [['1', '2', '3'],
                                     ['1.0', '8.0', '4'],
                                     ['1.0', '6', '7'],
                                     ['1.0', '8.0', '6'],
                                     ['1.0', '11', '12'],
                                     ['1.0', '13', '0']]
        cleaner = MeanDataCleaner()
        actual_list_after_clean = cleaner.clean_data(data=list_to_clean)
        self.assertEqual(expected_list_after_clean, actual_list_after_clean)


if __name__ == '__main__':
    unittest.main()
