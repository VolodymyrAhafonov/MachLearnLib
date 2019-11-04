import unittest
from unittest import mock

from utils.data.CsvTable import CsvTable
from utils.io.CsvReaderWriter import CsvReaderWriter


class test_CsvReader(unittest.TestCase):
    def test_CsvReader_read(self):
        # test non existing csv file
        with mock.patch('utils.io.CsvReaderWriter.CsvReaderWriter'):
            with mock.patch('os.path.exists', return_value=False):
                with self.assertRaises(Exception):
                    CsvReaderWriter.read('invalid.csv', with_header=False)

        # test valid csv with header
        TEST_TEXT = ['col1,col2,col3\n', '1,2,3\n']
        m = unittest.mock.mock_open(read_data=''.join(TEST_TEXT))
        m.return_value.__iter__ = lambda self: self
        m.return_value.__next__ = lambda self: next(iter(self.readline, ''))

        with mock.patch('utils.io.CsvReaderWriter.CsvReaderWriter'):
            with mock.patch('os.path.exists', return_value=True):
                with mock.patch('builtins.open', m):
                    csv_table = CsvReaderWriter.read('some_csv.csv', with_header=True)
                    self.assertEqual(['col1', 'col2', 'col3'], csv_table.header)
                    self.assertEqual([['1', '2', '3']], csv_table.data)

        # test valid csv without header
        with mock.patch('utils.io.CsvReaderWriter.CsvReaderWriter'):
            with mock.patch('os.path.exists', return_value=True):
                with mock.patch('builtins.open', m):
                    csv_table = CsvReaderWriter.read('some_csv.csv', with_header=False)
                    self.assertEqual(None, csv_table.header)
                    self.assertEqual([['col1', 'col2', 'col3'], ['1', '2', '3']], csv_table.data)

    def test_CsvReaderWriter_write(self):
        csv_table = CsvTable(header=['col1', 'col2', 'col3'], data=[['1', '2', '3'], ['4', '5', '6']])
        filepath = 'fake_path.csv'
        with mock.patch('builtins.open', mock.mock_open()) as mocked_file:
            CsvReaderWriter.write(filepath, csv_table)

            # assert if opened file on write mode 'w'
            mocked_file.assert_called_once_with(filepath, mode='w')

            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in file
            self.assertEqual(len(mocked_file().write.call_args_list), 3)
            mocked_file().write.aserrt_called_with('col1, col2, col3\r\n')
            mocked_file().write.aserrt_called_with('1, 2, 3\r\n')
            mocked_file().write.aserrt_called_with('4, 5, 6\r\n')


if __name__ == '__main__':
    unittest.main()
