# File: src/generate_data.py
# Purpose: Create a realistic fake climate dataset

import pandas as pd
import numpy as np

# Set a seed so results are the same every time
np.random.seed(42)

# Create dates from 1980 to 2023 (monthly)
dates = pd.date_range(start='1980-01-01', end='2023-12-01', freq='MS')

# Number of months
n = len(dates)

# Simulate temperature (slowly rising over time + seasonal variation)
trend = np.linspace(0, 2.5, n)           # global warming trend (+2.5°C over 40 years)
seasonal = 5 * np.sin(2 * np.pi * np.arange(n) / 12)  # seasons (summer/winter)
noise = np.random.normal(0, 0.5, n)      # random daily noise
temperature = 14 + trend + seasonal + noise  # base temp 14°C

# Simulate rainfall (mm)
rainfall = np.abs(np.random.normal(80, 30, n) + 10 * np.sin(2 * np.pi * np.arange(n) / 12))

# Simulate CO₂ levels (ppm) — steadily increasing
co2 = np.linspace(338, 420, n) + np.random.normal(0, 1, n)

# Simulate humidity (%)
humidity = np.clip(np.random.normal(65, 10, n), 30, 95)

# Inject some anomalies (unusual events)
# Example: a random heatwave in some months
anomaly_indices = np.random.choice(n, size=15, replace=False)
temperature[anomaly_indices] += np.random.uniform(3, 6, 15)

# Build the DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Temperature': np.round(temperature, 2),
    'Rainfall': np.round(rainfall, 2),
    'CO2_ppm': np.round(co2, 2),
    'Humidity': np.round(humidity, 2)
})

# Save to CSV
df.to_csv('data/climate_data.csv', index=False)
print("Dataset created! Shape:", df.shape)
print(df.head())