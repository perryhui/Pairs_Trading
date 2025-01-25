import pandas as pd
import numpy as np
from filterpy.kalman import KalmanFilter


import random
import csv

price_path = 'ticker_data_2010-01-01_2023-12-31.csv'
ratio_path = 'financial_ratio_data_2010-01-01_2023-12-31.csv'


# Load the csv into python for data processing
price_df = pd.read_csv(price_path, low_memory= False)
ratio_df = pd.read_csv(ratio_path, low_memory= False)

def Data_frame_processor(file_path):
    # Clean up some naming issues and combine the first two entries in every column
    df = pd.read_csv(file_path, low_memory= False, header= [0, 1])
    #Combine the first two rows as header
    df.columns = [' '.join([str(col1).strip(), str(col2).strip()]) if col1 else str(col2).strip() 
                  for col1, col2 in zip(df.columns.get_level_values(0), df.columns.get_level_values(1))]
    # Assign a header to the date column which will be indexed 
    df.rename(columns={'Unnamed: 0_level_0 Unnamed: 0_level_1': 'time_stamp'}, inplace=True)

    # Replace np.NaN wiht 0 int
    df = df.fillna(0)

    return df

price_ammended = Data_frame_processor(price_path)

print(price_ammended)



'''
def Data_frame_processor(file_path):
    # Clean up some naming issues and combine the first two entries in every column
    df = pd.read_csv(file_path, low_memory= False, header= [0, 1])
    df.columns = [' '.join([str(col1).strip(), str(col2).strip()]) if col1 else str(col2).strip() 
                  for col1, col2 in zip(df.columns.get_level_values(0), df.columns.get_level_values(1))]
    df.rename(columns={'Unnamed: 0_level_0 Unnamed: 0_level_1': 'time_stamp'}, inplace=True)
    # Disgard any column of data with more than 5% of missing value in the given time frame


    return df.copy()

price_ammended = Data_frame_processor(price_path)
print(price_ammended)

test = price_ammended['ZTF LN Equity VOLUME']

# Initialize Kalman filter
kf = KalmanFilter(dim_x=1, dim_z=1)

# Set the initial state (guess), variance, and other parameters
kf.x = np.array([test[0]])  # Initial state estimate is the first data point
kf.P = np.array([[1000]])  # Initial uncertainty
kf.F = np.array([[1]])  # State transition (assuming no change in state over time)
kf.H = np.array([[1]])  # Observation model (direct observation of the state)
kf.R = np.array([[1]])  # Measurement noise (can be adjusted)
kf.Q = np.array([[1e-5]])  # Process noise (small value)

# Create a list to store the estimated values
estimated_values = []

# Apply Kalman filter over the time series
for z in test:
    kf.predict()  # Prediction step
    
    if np.isnan(z):  # If the data is missing (NaN), use the predicted value
        estimated_values.append(kf.x[0])  # Use Kalman predicted value
    else:  # If the data is available, don't update; use the original value
        estimated_values.append(z)  # Keep the original data if available
        kf.update(z)  # Update the Kalman filter with the real measurement

# Convert the result back to a pandas Series
estimated_series = pd.Series(estimated_values, index=test.index)

# Add the estimated values to your DataFrame (it won't overwrite true values)
price_ammended['Estimated ZTF LN Equity VOLUME'] = estimated_series

# Show the DataFrame with the original and estimated columns
print(price_ammended[['ZTF LN Equity VOLUME', 'Estimated ZTF LN Equity VOLUME']])

price_ammended[['ZTF LN Equity VOLUME', 'Estimated ZTF LN Equity VOLUME']].to_csv('test.csv')

"""
def Kalman_Filter(data_frame):
    # Convert the timestamp column to datetime
    data_frame['time_stamp'] = pd.to_datetime(data_frame['time_stamp'])
    
    # Sort by timestamp and reset index
    data_frame = data_frame.sort_values(by='time_stamp').reset_index(drop=True)
    
    # Replace NaN, Inf, and -Inf with 0
    data_frame = data_frame.replace([np.inf, -np.inf, np.nan], 0)

    # Create a dictionary to store the smoothed columns
    smoothed_columns = {}

    # Loop over each feature/column (excluding 'time_stamp')
    for column in data_frame.columns:
        if column != 'time_stamp':  # Skip non-numeric columns
            feature_values = data_frame[column].values

            # Check if the feature is constant (this could cause issues)
            if np.std(feature_values) == 0:
                print(f"Warning: Feature {column} is constant and may cause issues.")
                continue  # Skip constant columns

            # Optionally scale the data
            scaler = StandardScaler()
            feature_values_scaled = scaler.fit_transform(feature_values.reshape(-1, 1)).flatten()

            # Initialize Kalman Filter
            kf = KalmanFilter(initial_state_mean=feature_values_scaled[0], n_dim_obs=1)
            
            # Set the transition and observation matrices (optional - defaults are typically fine)
            try:
                kf = kf.em(feature_values_scaled, n_iter=10)
                state_means, state_covariances = kf.filter(feature_values_scaled)
                
                # Store the Kalman smoothed values in the dictionary
                smoothed_columns[f'{column}_kalman_smoothed'] = state_means
            except Exception as e:
                print(f"Error applying Kalman filter to {column}: {e}")
                continue

    # Concatenate all smoothed columns at once
    smoothed_df = pd.DataFrame(smoothed_columns)

    # Join the smoothed columns to the original data
    data_frame = pd.concat([data_frame, smoothed_df], axis=1)

    # Display the first few rows of the updated dataframe
    return data_frame.copy()

price_processed = Kalman_Filter(price_ammended)
price_processed.head(10)


 

While there are imputation methodlogies used to fill in missing values in the data frame, 
it inevidently distorts the true distribution of data. Say for a example we have over 50% of data missing
from a stock, simple imputation methods with mean, mode, median assume that imputed values are similar to that
in the data set. We shall remove stocks with more than 5% of data in the given time frame


'''




