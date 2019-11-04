import csv
import os

from utils.data.CsvTable import CsvTable


class CsvReaderWriter:
    """
    Class that reads and writes csv tables
    """
    @staticmethod
    def read(path_to_csv_file: str, with_header: bool) -> CsvTable:
        if not os.path.exists(path_to_csv_file):
            raise Exception('Csv file ' + path_to_csv_file + ' doesnt exist')

        with open(path_to_csv_file) as csv_table:
            reader = csv.reader(csv_table)

        if with_header:
            header = next(reader)
        else:
            header = None
        data = []
        for row in reader:
            data.append(row)

        return CsvTable(header=header, data=data)

    @staticmethod
    def write(path_to_csv_file: str, csv_table: CsvTable) -> None:
        with open(path_to_csv_file, mode='w') as csv_file:
            writer = csv.writer(csv_file)
            if csv_table.header is not None:
                writer.writerow(csv_table.header)
            writer.writerows(csv_table.data)
