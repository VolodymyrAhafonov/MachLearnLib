from abc import ABC, abstractmethod
from typing import Dict, Tuple


HOLE_SYMBOLS = ['', '-', '?']


def is_float(s: str) -> bool:
    """
    Check if string is float.

    :param s: input string
    :return: True if s is number, False otherwise
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


class BaseDataCleaner(ABC):
    """
    Base class that clean input data(fill missing values and convert non numeric attributes to numeric attributes)
    """
    def __init__(self):
        pass

    @abstractmethod
    def clean_data(self, data: list) -> list:
        raise NotImplementedError

    @staticmethod
    def convert_nonnumeric_attributes_to_numeric(data: list) -> Tuple[list, Dict[int, str]]:
        """
        Convert nonnumeric attributes to numeric attributes.

        :param data: input data
        :return: tuple of converted data and dict where key - numeric value of attribute,
        value - nonnumeric value of proper attribute
        """
        attribute_map = {}
        current_attribute_value = 0

        rows = len(data)
        cols = len(data[0])

        for i in range(rows):
            for j in range(cols):
                elem = data[i][j]
                # check if element is not float and is not a hole symbol
                if not is_float(elem) and elem not in HOLE_SYMBOLS:
                    # check if symbolic attribute is already in map
                    if elem in attribute_map:
                        data[i][j] = str(attribute_map[elem])
                    else:
                        # symbolic attribute is not in attribute map, encode it to numeric and put in map
                        attribute_map[elem] = current_attribute_value
                        current_attribute_value += 1
                        data[i][j] = str(attribute_map[elem])

        result_dict = {}
        # invert attribute map
        for key in attribute_map.keys():
            result_dict[attribute_map[key]] = key

        return data, result_dict
