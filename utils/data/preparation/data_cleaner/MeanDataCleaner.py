import numpy as np

from utils.data.preparation.data_cleaner.BaseDataCleaner import BaseDataCleaner, HOLE_SYMBOLS


class MeanDataCleaner(BaseDataCleaner):
    """
    Data cleaner that fill holes by mean value across all value of attribute.
    """
    def clean_data(self, data: list) -> list:
        holes_coordinates = []
        column_accumulator = {}

        rows = len(data)
        cols = len(data[0])

        for i in range(rows):
            for j in range(cols):
                element = data[i][j]
                if element in HOLE_SYMBOLS:
                    holes_coordinates.append((i, j))
                else:
                    if j in column_accumulator:
                        column_accumulator[j].append(element)
                    else:
                        column_accumulator[j] = [element]

        # calculate mean for each column
        for key in column_accumulator.keys():
            column_accumulator[key] = np.mean(np.array(column_accumulator[key], dtype=np.float32))

        # fill holes
        for coords in holes_coordinates:
            data[coords[0]][coords[1]] = str(column_accumulator[coords[1]])

        return data
