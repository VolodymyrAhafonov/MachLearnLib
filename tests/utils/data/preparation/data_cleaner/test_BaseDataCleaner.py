import unittest

from utils.data.preparation.data_cleaner.BaseDataCleaner import BaseDataCleaner, is_float


class test_BaseDataCleaner(unittest.TestCase):
    def test_BasepDataCleaner(self):
        with self.assertRaises(TypeError):
            cleaner = BaseDataCleaner()

    def test_is_float(self):
        valid_float_number = '5.'
        expected_output = True
        actual_output = is_float(valid_float_number)
        self.assertEqual(expected_output, actual_output)

        valid_float_number = '71.5'
        expected_output = True
        actual_output = is_float(valid_float_number)
        self.assertEqual(expected_output, actual_output)

        valid_float_number = '12'
        expected_output = True
        actual_output = is_float(valid_float_number)
        self.assertEqual(expected_output, actual_output)

        invalid_float = 'invalid_number'
        expected_output = False
        actual_output = is_float(invalid_float)
        self.assertEqual(expected_output, actual_output)

    def test_BaseDataCleaner_convert_nonnumeric_attributes_to_numeric(self):
        data_list = [['1', '2', 'First_class'],
                     ['4', '0', 'Second_class'],
                     ['0', '102', 'First_class'],
                     ['?', '', 'Third_class'],
                     ['1', '-', 'Second_class']]
        expected_converted_data_list = [['1', '2', '0'],
                                        ['4', '0', '1'],
                                        ['0', '102', '0'],
                                        ['?', '', '2'],
                                        ['1', '-', '1']]
        expected_map = {0: 'First_class', 1: 'Second_class', 2: 'Third_class'}

        actual_converted_data_list, actual_map = BaseDataCleaner.convert_nonnumeric_attributes_to_numeric(data_list)
        self.assertEqual(expected_converted_data_list, actual_converted_data_list)
        self.assertTrue(expected_map, actual_map)


if __name__ == '__main__':
    unittest.main()
