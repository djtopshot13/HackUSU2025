import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('xgboost_training.csv')

# Encode categorical variables
le = LabelEncoder()
df['position'] = le.fit_transform(df['position'])

# Convert 'originNIL' and 'destinationNIL' to numeric
df['originNIL'] = pd.to_numeric(df['originNIL'], errors='coerce')
df['destinationNIL'] = pd.to_numeric(df['destinationNIL'], errors='coerce')

# Fill NaN values with median
df['originNIL'].fillna(df['originNIL'].median(), inplace=True)
df['destinationNIL'].fillna(df['destinationNIL'].median(), inplace=True)

# Prepare features and target
outboundfeatures = ['position', 'originNIL', 'origin21%', 'origin22%', 'origin23%', 
             'destinationNIL', 'stars']


X = df[outboundfeatures]
y = (df['destination'] != 'none').astype(int)  # 1 if destination is not 'none', 0 otherwise

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1)
model.fit(X_train, y_train)

# Make predictions and calculate MSE
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Feature importance
feature_importance = model.feature_importances_
importance_df = pd.DataFrame({'feature': outboundfeatures, 'importance': feature_importance})
importance_df = importance_df.sort_values('importance', ascending=False)
print("\nFeature Importance:")
print(importance_df)

# Function to predict on new data
def predict_transfers(new_data_path):
    new_df = pd.read_csv(new_data_path)
    new_df['position'] = le.transform(new_df['position'])
    new_df['originNIL'] = pd.to_numeric(new_df['originNIL'], errors='coerce')
    new_df['destinationNIL'] = pd.to_numeric(new_df['destinationNIL'], errors='coerce')
    new_df['originNIL'].fillna(new_df['originNIL'].median(), inplace=True)
    new_df['destinationNIL'].fillna(new_df['destinationNIL'].median(), inplace=True)
    X_new = new_df[outboundfeatures]
    predictions = model.predict(X_new)
    new_df['transfer_likelihood'] = predictions
    return new_df

# Example usage (uncomment when you have the PFF data file)
pff_data = predict_transfers('PFF Data\MW Data\pff-outbound.csv')
print(pff_data[['first_name', 'last_name', 'transfer_likelihood']].head())
