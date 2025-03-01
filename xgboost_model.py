import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

"""Step 1: Load the training data"""
df = pd.read_csv('xgboost_training.csv')

numeric_columns = df.select_dtypes(include=[np.number]).columns
categorical_columns = ['position', 'origin', 'destination', 'eligibility']

print("Numeric columns:", numeric_columns)
print("Categorical columns:", categorical_columns)

# Encode categorical variables
le = LabelEncoder()
for col in categorical_columns:
    df[col] = le.fit_transform(df[col].astype(str))

# Verify that all columns are now numeric
print(df.dtypes)

"""Cleaning and Preparing Data"""
# Convert categorical columns to numerical via one-hot encoding
# Ensure every piece of information is complete, remove empty rows
df_encoded = pd.get_dummies(df, columns=['transfer_date'], drop_first=True)

print("Encoded training data:")
print(df_encoded.head())

X = df.drop(['destination', 'player_id', 'first_name', 'last_name'], axis=1)
y = df_encoded['destination']  # Target variable

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

try:
    new_data = pd.read_csv('new_data.csv')
    
    # Apply the same encoding to new data
    for col in categorical_columns:
        if col in new_data.columns:
            new_data[col] = le.transform(new_data[col].astype(str))
    
    # Ensure all columns in new_data match X
    new_data = new_data.reindex(columns=X.columns, fill_value=0)
    
    # Predict
    new_data['Risk'] = model.predict(new_data)
    
    # Save results
    new_data.to_csv('new_data_with_risk.csv', index=False)
    print("New data with risk predictions saved to 'new_data_with_risk.csv'.")
except FileNotFoundError:
    print("new_data.csv not found. Skipping prediction on new data.")
