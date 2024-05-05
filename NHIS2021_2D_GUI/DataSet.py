import pandas as pd

class DataSet:
    @staticmethod
    def load_data(dataset_url, index_col=None):
        data = pd.read_csv(dataset_url, index_col=index_col)
        return data
