import pandas as pd
import numpy as np
# Load the csv into python for data processing
price_df = pd.read_csv('ticker_data_2010-01-01_2023-12-31.csv', low_memory= False)
volume_df = pd.read_csv('volume_data_2010-01-01_2023-12-31.csv', low_memory= False)
ratio_df = pd.read_csv('financial_ratio_data_2010-01-01_2023-12-31.csv', low_memory= False)

'''
While there are imputation methodlogies used to fill in missing values in the data frame, 
it inevidently distorts the true distribution of data. Say for a example we have over 50% of data missing
from a stock, simple imputation methods with mean, mode, median assume that imputed values are similar to that
in the data set. We shall remove stocks with more than 5% of data in the given time frame
'''

# Calculate the percentage of missing price values in each column (stock)
price_missing_percentage = price_df.isnull().mean() * 100

# Filter out columns with more than 5% missing values
price_df_cleaned = price_df.loc[:, price_missing_percentage <= 5]

#Do the same for financial ratio 

ratio_missing_percentage = ratio_df.isnull().mean() * 100

ratio_df_cleaned = ratio_df.loc[:, ratio_missing_percentage <= 5]

# combine cleaned price df with volume data
price_vol_df_cleaned = price_df_cleaned.join(volume_df)

#Data Imputation





