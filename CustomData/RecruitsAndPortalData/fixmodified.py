import pandas as pd
df = pd.read_csv('modified_CFB_Portal_Data.csv')

# Remove $ and , then convert 'none' to NaN
df['destinationNIL'] = df['destinationNIL'].astype(str).replace({'\$': '', ',': '', 'none': ''}, regex=True)
df['originNIL'] = df['originNIL'].astype(str).replace({'\$': '', ',': '', 'none': ''}, regex=True)

# Convert to numeric, setting errors='coerce' to turn invalid values into NaN
df['destinationNIL'] = pd.to_numeric(df['destinationNIL'], errors='coerce').fillna(0).astype(int)
df['originNIL'] = pd.to_numeric(df['originNIL'], errors='coerce').fillna(0).astype(int)

df.to_csv('modified_CFB_Portal_Data.csv', index=False)