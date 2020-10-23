import pandas as pd
import numpy as np

def create_diabetes_dataframe():
    df = pd.read_csv('diabetes_data.csv')
    df.drop(columns=['class'], inplace=True)
    return df
