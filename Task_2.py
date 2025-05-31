import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the CSV
df = pd.read_csv("delhiaqi.csv")

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract time-based features
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df['weekday'] = df['date'].dt.day_name()

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# --- Add AQI Category based on PM2.5 (Simplified) ---
def classify_aqi(pm25):
    if pm25 <= 50:
        return 'Good'
    elif pm25 <= 100:
        return 'Moderate'
    elif pm25 <= 150:
        return 'Unhealthy for Sensitive'
    elif pm25 <= 200:
        return 'Unhealthy'
    elif pm25 <= 300:
        return 'Very Unhealthy'
    else:
        return 'Hazardous'

df['AQI_Category'] = df['pm2_5'].apply(classify_aqi)

# Export cleaned data
df.to_excel("cleaned_delhi_aqi.xlsx", index=False)

# --- Plot 1: PM2.5 by Hour ---
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='hour', y='pm2_5', estimator='mean', errorbar=None)
plt.title("Average PM2.5 by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("PM2.5")
plt.tight_layout()
plt.savefig("pm2_5_by_hour.png")
plt.clf()

# --- Plot 2: PM2.5 by Month ---
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='month', y='pm2_5')
plt.title("PM2.5 Distribution by Month")
plt.xlabel("Month")
plt.ylabel("PM2.5")
plt.tight_layout()
plt.savefig("pm2_5_by_month.png")
plt.clf()

# --- Plot 3: Correlation Heatmap ---
plt.figure(figsize=(10, 6))
corr = df[['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Pollutants")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.clf()

# --- Plot 4: Pollutants by Hour ---
plt.figure(figsize=(12, 6))
for pollutant in ['pm2_5', 'pm10', 'co', 'no', 'no2', 'o3', 'so2', 'nh3']:
    sns.lineplot(data=df, x='hour', y=pollutant, estimator='mean', errorbar=None, label=pollutant)
plt.title("Pollutant Levels by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Concentration")
plt.legend()
plt.tight_layout()
plt.savefig("all_pollutants_by_hour.png")
plt.clf()

# --- Plot 5: PM2.5 by Day of Week ---
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='weekday', y='pm2_5', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title("PM2.5 Levels by Day of Week")
plt.xlabel("Day")
plt.ylabel("PM2.5")
plt.tight_layout()
plt.savefig("pm2_5_by_day.png")
plt.clf()

# --- Plot 6: AQI Category Distribution ---
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='AQI_Category', hue='AQI_Category', order=df['AQI_Category'].value_counts().index, palette='coolwarm', legend=False)
plt.title("AQI Category Distribution Based on PM2.5")
plt.xlabel("AQI Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("aqi_category_distribution.png")
plt.clf()

print("✅ All enhanced plots and Excel export generated successfully.")
