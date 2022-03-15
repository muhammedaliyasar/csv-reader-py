import csv
import pandas as pd

class CsvReader():
    """
        csv file reader
    """
    def __init__(self, file_name):
        """
            file_name = csv file name
        """
        self.file_name = file_name
        self.data_frame = pd.read_csv(f"{file_name}")

    def showDataFrame(self):
        """
            returns data frame
        """
        print(self.data_frame)

