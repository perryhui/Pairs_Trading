import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import random
import csv

price_path = 'ticker_data_2010-01-01_2023-12-31.csv'
ratio_path = 'financial_ratio_data_2010-01-01_2023-12-31.csv'


# Load the csv into python for data processing
price_df = pd.read_csv(price_path, low_memory= False)
ratio_df = pd.read_csv(ratio_path, low_memory= False)

data_frames = [price_df, ratio_df]

def Data_frame_processor(file_path):
    # Clean up some naming issues and combine the first two entries in every column
    df = pd.read_csv(file_path, low_memory= False, header= [0, 1])
    df.columns = [' '.join([str(col1).strip(), str(col2).strip()]) if col1 else str(col2).strip() 
                  for col1, col2 in zip(df.columns.get_level_values(0), df.columns.get_level_values(1))]
    df.rename(columns={'Unnamed: 0_level_0 Unnamed: 0_level_1': 'Date'}, inplace=True)

    # Disgard any column of data with more than 5% of missing value in the given time frame
    


    return df



price_cleaned_df = Data_frame_processor(price_path)
ratio_cleaned_df = Data_frame_processor(ratio_path)





'''
While there are imputation methodlogies used to fill in missing values in the data frame, 
it inevidently distorts the true distribution of data. Say for a example we have over 50% of data missing
from a stock, simple imputation methods with mean, mode, median assume that imputed values are similar to that
in the data set. We shall remove stocks with more than 5% of data in the given time frame


# Data Imputation: We use linear regression and stochastic imputation to impute the missing values 
# We spilt the dataframe into to sub-dataframes: 
# Rows without missing values (to train the regression model).
# Rows with missing values (to predict the missing data).
# Stochastic imputation is used to adding randomness in the imputed data
'''




