import pandas as pd
import numpy as np
#Load the csv into python for data processing
df = pd.read_csv('ticker_data_2010-01-01_2023-12-31.csv', low_memory= False)

'''
While there are imputation methodlogies used to fill in missing values in the data frame, 
it inevidently distorts the true distribution of data. Say for a example we have over 50% of data missing
from a stock, simple imputation methods with mean, mode, median assume that imputed values are similar to that
in the data set. Given that data is from Bloomberg, the only reason for missing data is perhaps that the stock has not been listed 
for the entirety of the time frame. Hence we shall remove stocks with more than 5% of data in the given time frame
'''

# Calculate the percentage of missing values in each column (stock)
missing_percentage = df.isnull().mean() * 100

# Filter out columns with more than 5% missing values
df_cleaned = df.loc[:, missing_percentage <= 5]

'''
We have filtered out 84 stocks that do not satisfy the criteria
We shall now use imputation to fill in the missing value

'''


