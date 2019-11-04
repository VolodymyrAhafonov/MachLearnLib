import unittest

from utils.data.preparation.data_cleaner.DropDataCleaner import DropDataCleaner
from utils.data.preparation.data_cleaner.BaseDataCleaner import HOLE_SYMBOLS


class test_DropDataCleaner(unittest.TestCase):
    def test_DropDataCleaner_clean_data(self):
        list_to_clean = [['1', '2', '3'],
                         ['4', HOLE_SYMBOLS[0], HOLE_SYMBOLS[1]],
                         ['5', '6', '7'],
                         [HOLE_SYMBOLS[0], HOLE_SYMBOLS[2], HOLE_SYMBOLS[1]],
                         ['10', '11', '12'],
                         ['12', '13', HOLE_SYMBOLS[1]]]

        expected_list_after_clean = [['1', '2', '3'],
                                     ['5', '6', '7'],
                                     ['10', '11', '12']]
        cleaner = DropDataCleaner()
        actual_list_after_clean = cleaner.clean_data(data=list_to_clean)
        self.assertEqual(expected_list_after_clean, actual_list_after_clean)


if __name__ == '__main__':
    unittest.main()
