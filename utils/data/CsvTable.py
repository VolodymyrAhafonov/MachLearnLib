import numpy as np

from utils.data.preparation.data_cleaner.BaseDataCleaner import BaseDataCleaner


class CsvTable:
    """
    Class that handle csv table data.
    """
    def __init__(self, header: list or None, data_rows: list):
        self.__header = header
        self.__data = data_rows

    def to_numpy(self, dtype: np.dtype) -> np.ndarray:
        return np.array(self.data, dtype=dtype)

    def fill_holes(self, data_cleaner: BaseDataCleaner):  # return CsvTable
        data = data_cleaner.clean_data(self.__data.copy())
        return CsvTable(header=self.header, data_rows=data)

    def convert_nonnumeric_attributes_to_numeric(self):  # return Tuple[CsvTable, Dict[int, str]]
        data, attribute_map = BaseDataCleaner.convert_nonnumeric_attributes_to_numeric(self.__data.copy())
        return CsvTable(header=self.__header, data_rows=data), attribute_map

    @property
    def header(self):
        return self.__header

    @property
    def data(self):
        return self.__data
