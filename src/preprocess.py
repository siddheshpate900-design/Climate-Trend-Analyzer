# File: src/preprocess.py
# Purpose: Load and clean the climate dataset

import pandas as pd

# Load the data
df = pd.read_csv('data/climate_data.csv')

print("--- Before Cleaning ---")
print(df.isnull().sum())   # check for missing values
print(df.dtypes)           # check data types

# Convert Date to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Add useful columns
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Fill any missing values with the column average
df.fillna(df.mean(numeric_only=True), inplace=True)

# Save cleaned data
df.to_csv('data/cleaned_climate_data.csv', index=False)
print("\n--- After Cleaning ---")
print(df.head())
print("Cleaned data saved!")