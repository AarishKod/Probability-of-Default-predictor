"""By Aarish Kodnaney"""

from typing import Any
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

def load_dataset(source_as_path: str) -> DataFrame:
    """Loads the dataset"""
    return pd.read_csv(source_as_path)

def build_histogram_of_FICO_scores(dataset_FICO: Series) -> None:
    """
    builds a histogram of fico scores using matplotlib
    """
    data_for_analysis = dataset_FICO
    plt.hist(data_for_analysis, bins=5, color='skyblue', edgecolor='black')
    plt.xlabel('FICO scores')
    plt.ylabel("Frequency")
    plt.title("Distribution of FICO scores")
    plt.show()

def create_buckets(dataset_fico: Series) -> Any:
    """"""
    return pd.qcut(dataset_fico, 10, labels=['Tier 1', 'Tier 2', 'Tier 3', 'Tier 4', 'Tier 5','Tier 6', 'Tier 7', 'Tier 8', 'Tier 9', 'Tier 10'], retbins=False)


data: DataFrame = load_dataset("Task 3 and 4_Loan_Data.csv")


print(data["fico_score"].describe())

df_buckets = pd.DataFrame({
    'fico': data["fico_score"],
    'default': data["default"]
})
df_buckets['bucket'] = create_buckets(df_buckets['fico'])

default_rates = df_buckets.groupby('bucket')['default'].mean()
print(default_rates)



# print(df_buckets)
