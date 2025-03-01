import pandas as pd

# Read existing CSV
nil = pd.read_csv("/Users/lukenichols/Documents/GitHub/HackUSU2025/CustomData/NILData/NILGroupof5.csv")

# Dictionary of private schools and their conferences
private = {
    'Rice': 'American',
    'Temple': 'American',
    'Tulane': 'American',
    'Tulsa': 'American',
    'Akron': 'MAC',
    'Jacksonville State': 'CUSA',
    'Liberty': 'CUSA',
    'Louisiana Tech': 'CUSA',
    'Middle Tennessee State': 'CUSA'
}

# Update 'Collective Funding' for existing private schools
for school in private.keys():
    nil.loc[nil['School'] == school, 'Collective Funding'] = 1471894  # Assign new value

# Ensure 'Collective Funding' is a string before replacing unwanted characters
nil['Collective Funding'] = nil['Collective Funding'].astype(str).str.replace(r'[\$,]', '', regex=True)

# Convert 'Collective Funding' to numeric (handle NaNs properly)
nil['Collective Funding'] = pd.to_numeric(nil['Collective Funding'], errors='coerce')

# If you want all values as integers and fill NaNs with 0 (optional)
nil['Collective Funding'] = nil['Collective Funding'].fillna(0).astype(int)

# Save the updated DataFrame to a new CSV file
nil.to_csv("/Users/lukenichols/Documents/GitHub/HackUSU2025/CustomData/NILData/NILGroupof5_Updated.csv", index=False)

