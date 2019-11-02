import unittest

import numpy as np

from utils.data.CsvTable import CsvTable
from utils.data.preparation.data_cleaner.BaseDataCleaner import HOLE_SYMBOLS
from utils.data.preparation.data_cleaner.DropDataCleaner import DropDataCleaner


class TestCsvTable(unittest.TestCase):
    def test_CsvTable_properties(self):
        header = ['first', 'second', 'third']
        data = [['1', '2', '3',
                 '4', '5', '6']]
        csv_table = CsvTable(header=header, data=data)
        self.assertEqual(header, csv_table.header)
        self.assertEqual(data, csv_table.data)

        # try to set read only attribute
        with self.assertRaises(AttributeError):
            csv_table.data = None

        # try to set read only attribute
        with self.assertRaises(AttributeError):
            csv_table.header = None

    def test_CsvTable_to_numpy(self):
        header = ['first', 'second', 'third']
        data = [['1.1', '2.3', '3'],
                ['4', '5', '6.5']]
        csv_table = CsvTable(header=header, data=data)
        expected_numpy_arr = np.array([[1.1, 2.3, 3], [4, 5, 6.5]], dtype=np.float32)
        actual_numpy_arr = csv_table.to_numpy(dtype=np.float32)
        self.assertTrue(np.array_equal(expected_numpy_arr, actual_numpy_arr))

        expected_numpy_arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.uint8)
        actual_numpy_arr = csv_table.to_numpy(dtype=np.uint8)
        self.assertTrue(np.array_equal(expected_numpy_arr, actual_numpy_arr))

    def test_CsvTable__eq__(self):

        # check equal tables
        header = ['first, second, third']
        data = [['1', '2', '3'],
                ['4', '5', '6']]

        first_csv_table = CsvTable(header=header.copy(), data=data.copy())
        second_csv_table = CsvTable(header=header.copy(), data=data.copy())
        self.assertTrue(first_csv_table == second_csv_table)

        # check with unequal header
        other_header = ['first', 'second', 'not_third']
        first_csv_table = CsvTable(header=header.copy(), data=data.copy())
        second_csv_table = CsvTable(header=other_header.copy(), data=data.copy())
        self.assertFalse(first_csv_table == second_csv_table)

        # check with unequal data
        other_data = [['1', '2', '3'],
                      ['4', '5', '?']]
        first_csv_table = CsvTable(header=header.copy(), data=data.copy())
        second_csv_table = CsvTable(header=header.copy(), data=other_data.copy())
        self.assertFalse(first_csv_table == second_csv_table)

        # check with other object
        first_csv_table = CsvTable(header=header.copy(), data=data.copy())
        second = object
        self.assertFalse(first_csv_table == second)

    def test_CsvTable_convert_nonnumeric_attributes_to_numeric(self):
        header = None
        data_list = [['1', '2', 'First_class'],
                     ['4', '0', 'Second_class'],
                     ['0', '102', 'First_class'],
                     ['?', '', 'Third_class'],
                     ['1', '-', 'Second_class']]
        csv_table = CsvTable(header=header, data=data_list)

        expected_converted_data_list = [['1', '2', '0'],
                                        ['4', '0', '1'],
                                        ['0', '102', '0'],
                                        ['?', '', '2'],
                                        ['1', '-', '1']]
        expected_csv_table = CsvTable(header=header, data=expected_converted_data_list)
        expected_map = {0: 'First_class', 1: 'Second_class', 2: 'Third_class'}

        actual_csv_table, actual_map = csv_table.convert_nonnumeric_attributes_to_numeric()
        self.assertEqual(expected_csv_table, actual_csv_table)
        self.assertTrue(expected_map, actual_map)

    def test_CsvTable_clean_data(self):
        header = None
        data_list_to_clean = [['1', '2', '3'],
                              ['4', HOLE_SYMBOLS[0], HOLE_SYMBOLS[1]],
                              ['5', '6', '7'],
                              [HOLE_SYMBOLS[0], HOLE_SYMBOLS[2], HOLE_SYMBOLS[1]],
                              ['10', '11', '12'],
                              ['12', '13', HOLE_SYMBOLS[1]]]
        csv_table = CsvTable(header=header, data=data_list_to_clean)

        expected_data_list_after_clean = [['1', '2', '3'],
                                          ['5', '6', '7'],
                                          ['10', '11', '12']]
        expected_csv_after_clean = CsvTable(header=header, data=expected_data_list_after_clean)

        cleaner = DropDataCleaner()
        actual_csv_after_clean = csv_table.clean_data(data_cleaner=cleaner)
        self.assertEqual(expected_csv_after_clean, actual_csv_after_clean)


if __name__ == '__main__':
    unittest.main()
