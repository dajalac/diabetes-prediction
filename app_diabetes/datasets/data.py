import pandas as pd
import pathlib
import pickle
from sklearn.ensemble import RandomForestClassifier
from joblib import load

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
    model = pickle.load(open(DATA_PATH.joinpath('classification_model.pkl'),'rb'))
    #model = load(filename=DATA_PATH.joinpath("random_forest_model.joblib"))
    return model

def get_accuracy():
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("../datasets")
    accuracy = pickle.load(open(DATA_PATH.joinpath('model_accuracy.pkl'), 'rb'))
    return accuracy

