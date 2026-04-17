# File: src/anomaly_detection.py
# Purpose: Find unusual climate events

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned_climate_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Calculate mean and standard deviation
mean_temp = df['Temperature'].mean()
std_temp = df['Temperature'].std()

# Any temperature more than 2 standard deviations above average = anomaly
df['Anomaly'] = df['Temperature'] > (mean_temp + 2 * std_temp)

# Show anomalies
anomalies = df[df['Anomaly']]
print(f"Found {len(anomalies)} temperature anomalies!")
print(anomalies[['Date', 'Temperature']])

# Save anomaly table
anomalies[['Date', 'Temperature']].to_csv('outputs/anomalies.csv', index=False)

# Plot
plt.figure(figsize=(14, 5))
plt.plot(df['Date'], df['Temperature'], color='steelblue', alpha=0.5)
plt.scatter(anomalies['Date'], anomalies['Temperature'], color='red', label='Anomaly', zorder=5)
plt.axhline(mean_temp + 2*std_temp, color='orange', linestyle='--', label='Threshold')
plt.title('Temperature Anomaly Detection')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/anomaly_detection.png')
plt.show()
print("Anomaly graph saved!")