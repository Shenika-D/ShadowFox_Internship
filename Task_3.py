import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Load data
df = pd.read_csv("car_model_dataset.csv")

# Drop duplicates
df.drop_duplicates(inplace=True)

# Drop 'Model' as it's highly granular
df.drop(columns=['Model'], inplace=True)

# Visualize missing data
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values in Dataset")
plt.savefig("missing_values_heatmap.png")

# Separate features and target
X = df.drop(columns=["MSRP"])
y = df["MSRP"]

# Identify categorical and numerical columns
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

# Preprocessing for numerical data
numerical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# Combine preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_transformer, numerical_cols),
        ("cat", categorical_transformer, categorical_cols)
    ]
)

# Create pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Correlation matrix (only for numerical features including target)
plt.figure(figsize=(12, 8))
sns.heatmap(df[numerical_cols + ["MSRP"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig("correlation_matrix.png")

# MSRP distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["MSRP"], bins=50, kde=True)
plt.title("Distribution of MSRP")
plt.xlabel("MSRP")
plt.savefig("msrp_distribution.png")

# Boxplot of MSRP by Vehicle Size
plt.figure(figsize=(10, 6))
sns.boxplot(x="Vehicle Size", y="MSRP", data=df)
plt.title("MSRP by Vehicle Size")
plt.savefig("msrp_by_vehicle_size.png")

# Pairplot (only select top features to avoid overplotting)
selected_features = ["Engine HP", "Engine Cylinders", "highway MPG", "city mpg", "MSRP"]
sns.pairplot(df[selected_features].dropna())
plt.suptitle("Pairplot of Selected Features", y=1.02)
plt.savefig("selected_features_pairplot.png")
