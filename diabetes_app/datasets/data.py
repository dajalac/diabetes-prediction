import pandas as pd
import pathlib
import pickle


def create_diabetes_dataframe():
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("../datasets")
    df = pd.read_csv(DATA_PATH.joinpath('diabetes_data.csv'))
    df.rename(columns={'class': 'Diabetes'}, inplace=True)
    return df


def create_rows_coordinates():
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("../datasets")
    df = pd.read_csv(DATA_PATH.joinpath('mca_rows_coordinates.csv'))
    df.rename(columns={'class':'Diabetes'}, inplace=True)
    return df

def get_model():
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("../datasets")
    model = pickle.load(open('classification_model.sav','rb'))
    return model

print(get_model())
