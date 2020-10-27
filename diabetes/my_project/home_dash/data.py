import pandas as pd
import numpy as np
#todo check how open files whithout need to put the entire path

def create_diabetes_dataframe():
    df = pd.read_csv('D:\WGU\Capstone\AjalaCruz-D\diabetes\my_project\home_dash\diabetes_data.csv')
    df.rename(columns={'class': 'Diabetes'}, inplace=True)
    return df

def create_cat_dataframe():
    df = pd.read_csv('D:\WGU\Capstone\AjalaCruz-D\diabetes\my_project\home_dash\data_in_cat.csv.csv')
    df.drop(columns=['class'], inplace=True)
    return df

def create_numeric_dataframe():
    df = pd.read_csv('D:\WGU\Capstone\AjalaCruz-D\diabetes\my_project\home_dash\data_numeric.csv.csv')
    df.drop(columns=['class'], inplace=True)
    return df

def create_columns_coordinates():
    df = pd.read_csv('D:\WGU\Capstone\AjalaCruz-D\diabetes\my_project\home_dash\mca_columns_coordinates.csv')
    df.drop(columns=['class'], inplace=True)
    return df
def create_rows_coordinates():
    df = pd.read_csv('D:\WGU\Capstone\AjalaCruz-D\diabetes\my_project\home_dash\mca_rows_coordinates.csv')
    df.rename(columns={'class':'Diabetes'},inplace=True)
    return df
