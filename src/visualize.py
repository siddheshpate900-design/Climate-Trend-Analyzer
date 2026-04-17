# File: src/visualize.py
# Purpose: Create climate trend visualizations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/cleaned_climate_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# ---- Graph 1: Temperature Over Time ----
plt.figure(figsize=(14, 5))
plt.plot(df['Date'], df['Temperature'], alpha=0.5, color='Purple', label='Monthly Temp')
df['Rolling_Avg'] = df['Temperature'].rolling(window=12).mean()
plt.plot(df['Date'], df['Rolling_Avg'], color='red', linewidth=2, label='12-Month Average')
plt.title('Global Temperature Trend (1980–2023)')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/temperature_trend.png')
plt.show()
print("Graph 1 saved!")

# ---- Graph 2: CO2 Levels Rising ----
plt.figure(figsize=(14, 4))
plt.plot(df['Date'], df['CO2_ppm'], color='orange')
plt.title('CO₂ Concentration Over Time')
plt.xlabel('Year')
plt.ylabel('CO₂ (ppm)')
plt.tight_layout()
plt.savefig('outputs/co2_trend.png')
plt.show()
print("Graph 2 saved!")

# ---- Graph 3: Monthly Heatmap ----
pivot = df.pivot_table(index='Month', columns='Year', values='Temperature')
plt.figure(figsize=(20, 6))
sns.heatmap(pivot, cmap='coolwarm', linewidths=0.1)
plt.title('Monthly Temperature Heatmap (All Years)')
plt.tight_layout()
plt.savefig('outputs/temperature_heatmap.png')
plt.show()
print("Graph 3 saved!")

# ---- Graph 4: Rainfall Variation ----
plt.figure(figsize=(14, 4))
plt.bar(df['Date'], df['Rainfall'], color='teal', alpha=0.6)
plt.title('Monthly Rainfall (1980–2023)')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')
plt.tight_layout()
plt.savefig('outputs/rainfall_trend.png')
plt.show()
print("Graph 4 saved!")