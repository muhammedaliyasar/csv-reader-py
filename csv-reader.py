import pandas as pd

class CsvReader():
    """
        Excel reader
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_frame = pd.read_csv(f"{file_name}")

    def showDataFrame(self):
        print(self.data_frame)


