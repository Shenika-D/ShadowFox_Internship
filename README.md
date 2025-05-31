# ShadowFox Internship Projects

This repository contains the project submissions for my Data Science Internship at ShadowFox, covering real-world data analysis and documentation using Python. The tasks demonstrate proficiency in data visualization, exploratory data analysis, and model development using structured datasets and visualization libraries.

---

## 📁 Task 1: Visualization Library Documentation (Matplotlib & Seaborn)

### 📌 Objective
To create comprehensive documentation for two Python visualization libraries — **Matplotlib** and **Seaborn** — highlighting their capabilities, strengths, and best-use scenarios.

### 🔍 Highlights
- Provided a **library overview** discussing the purpose, design philosophy, and strengths of Matplotlib and Seaborn.
- Documented multiple types of graphs:
  - **Line plots**
  - **Bar charts**
  - **Histograms**
  - **Pie charts**
  - **Scatter plots**
  - **Box plots**
  - **Heatmaps**
- Included **real Python code snippets** with every chart type for demonstration.
- Concluded with a **comparison** of the libraries focusing on:
  - Ease of use
  - Aesthetic output
  - Interactivity
  - Suitability for large datasets

### 🧾 Key Insights
- **Matplotlib** offers granular control and is ideal for highly customized static plots.
- **Seaborn** simplifies statistical plotting with cleaner syntax and attractive default themes.
- Seaborn is better for rapid exploratory analysis, while Matplotlib is better suited for publication-quality visuals.

---

## 📁 Task 2: Analyzing the Air Quality Index in Delhi

### 📌 Objective
To perform a detailed analysis of the **Air Quality Index (AQI)** in Delhi using pollutant concentration data. The aim is to uncover patterns in pollution levels across different times and assess the severity and sources of pollution.

### 🔍 Highlights
- Cleaned and preprocessed a dataset containing hourly readings of pollutants including PM2.5, PM10, NO, NO₂, SO₂, CO, NH₃, and O₃.
- Extracted time-based features (hour, weekday, month) and classified AQI levels based on PM2.5 concentration.
- Created visualizations using Seaborn and Matplotlib to analyze:
  - Diurnal and weekly variations in PM2.5
  - Seasonal trends in air pollution
  - Correlations between pollutants
  - AQI category distribution
- Exported the cleaned dataset as an Excel file for future use.

### 📊 Visuals
- `pm2_5_by_hour.png`
- `pm2_5_by_day.png`
- `pm2_5_by_month.png`
- `correlation_heatmap.png`
- `all_pollutants_by_hour.png`
- `aqi_category_distribution.png`

### 🧾 Key Insights
- "Hazardous" AQI conditions are frequently observed, especially on weekdays.
- PM2.5 and PM10 levels are highest during mid-day and early week.
- Strong correlations suggest shared pollution sources like traffic and industrial emissions.

---

## 📁 Task 3: Exploring Car Characteristics and Pricing in India

### 📌 Objective
To analyze vehicle characteristics and evaluate their influence on car pricing (MSRP) in the Indian automotive market using statistical methods and machine learning.

### 🔍 Highlights
- Cleaned the dataset and handled missing values in columns like `Engine HP`, `Engine Cylinders`, and `Number of Doors`.
- Visualized feature distributions and relationships using:
  - Histograms
  - Boxplots
  - Pairplots
  - Correlation matrices
- Built a **Linear Regression** model to predict MSRP based on engine specifications.
- Evaluated model performance using:
  - R² Score
  - Mean Squared Error (MSE)
  - Residual analysis

### 📊 Visuals
- `msrp_distribution.png`
- `correlation_matrix.png`
- `selected_features_pairplot.png`
- `residual_plot.png`
- `msrp_by_vehicle_size.png`

### 🧾 Key Insights
- MSRP is highly **right-skewed** with notable high-end outliers.
- Engine HP, Cylinders, and Vehicle Size are **strong predictors** of price.
- Linear regression model achieved an **R² score of 0.93**, showing good predictive power.

---

## 🛠️ Technologies Used
- Python
- Jupyter Notebook & PyCharm
- Pandas, NumPy
- Matplotlib, Seaborn
- scikit-learn

---

## 📂 Repository Structure
