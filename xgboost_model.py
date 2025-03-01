import pandas as pd

"""Step 1: Load the training data"""
df = pd.read_csv('xgboost_training.csv')

"""Cleaning and Preparing Data"""
# Convert categorical columns to numerical via one-hot encoding
# Ensure every piece of information is complete, remove empty rows
df_encoded = pd.get_dummies(df, columns=['targetvariable1', 'targetvariable2'], drop_first=True)

print("Encoded training data:")
print(df_encoded.head())

X = df_encoded.drop('target', axis=1)  # Drop target columns from features
y = df_encoded['target']  # Target variable

"""Step 2: Split data for training and testing"""
from sklearn.model_selection import train_test_split

rs = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rs)

"""Step 3: Train Model"""
import xgboost as xgb

model = xgb.XGBRegressor(use_label_encoder=False, eval_metric='mlogloss')

model.fit(X_train, y_train)

# Predict using the test set (you can also use the test set to evaluate performance)
y_pred = model.predict(X_test)

"""Step 4: Evaluate Model Performance"""
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

"""Step 5: Predict Risk for the new data (new_data.csv)"""
# Load the new data (this should have the same features as the training data)
new_data = pd.read_csv('new_data.csv')

# Make sure to apply the same preprocessing (e.g., one-hot encoding) to the new data
new_data_encoded = pd.get_dummies(new_data, columns=['targetvariable1', 'targetvariable2'], drop_first=True)

# Align the columns to make sure the new data matches the training data's feature set
new_data_encoded = new_data_encoded.reindex(columns=X.columns, fill_value=0)

"""Step 6: Predict the likelihood to leave (Risk)"""
new_data['Risk'] = model.predict(new_data_encoded)

"""Step 7: Save the new data with the Risk column"""
new_data.to_csv('new_data_with_risk.csv', index=False)

print("New data with risk predictions saved to 'new_data_with_risk.csv'.")