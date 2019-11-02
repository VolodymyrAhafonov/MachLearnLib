import numpy as np

from utils.data.preparation.data_cleaner.BaseDataCleaner import BaseDataCleaner


class CsvTable:
    """
    Class that handle csv table data.
    """
    def __init__(self, header: list or None, data: list):
        self.__header = header
        self.__data = data

    def to_numpy(self, dtype: np.generic) -> np.ndarray:
        return np.array(self.data, dtype=np.float32).astype(dtype)

    def fill_holes(self, data_cleaner: BaseDataCleaner):  # return CsvTable
        data = data_cleaner.clean_data(self.__data.copy())
        return CsvTable(header=self.header, data=data)

    def convert_nonnumeric_attributes_to_numeric(self):  # return Tuple[CsvTable, Dict[int, str]]
        data, attribute_map = BaseDataCleaner.convert_nonnumeric_attributes_to_numeric(self.__data.copy())
        return CsvTable(header=self.__header, data=data), attribute_map

    @property
    def header(self):
        return self.__header

    @property
    def data(self):
        return self.__data

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.__dict__ == other.__dict__
