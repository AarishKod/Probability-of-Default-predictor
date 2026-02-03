"""By Aarish Kodnaney"""
import pandas as pd
from pandas import DataFrame

def load_dataset(source_as_path: str) -> DataFrame:
    """Loads the dataset"""
    return pd.read_csv(source_as_path)





class Bucket:
    def __init__(self, number_of_buckets: int, ):
        pass