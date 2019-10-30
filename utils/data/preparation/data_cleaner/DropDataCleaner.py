import numpy as np

from utils.data.preparation.data_cleaner.BaseDataCleaner import BaseDataCleaner, HOLE_SYMBOLS


class DropDataCleaner(BaseDataCleaner):
    """
    Data cleaner that drop vectors that have one or more holes in it.
    """
    def clean_data(self, data: list) -> list:
        holes_coordinates = []

        rows = len(data)
        cols = len(data[0])

        for i in range(rows):
            for j in range(cols):
                element = data[i][j]
                if element in HOLE_SYMBOLS:
                    holes_coordinates.append(i)
                    break

        holes_coordinates = np.array(holes_coordinates, dtype=np.int32)
        for hole_coordinate in holes_coordinates:
            del data[hole_coordinate]
            # correct coordinates cause list len decrease by one when item is deleted
            holes_coordinates -= 1

        return data
