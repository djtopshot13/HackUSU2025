import pandas as pd

# Read existing CSV
nil = pd.read_csv("/Users/lukenichols/Documents/GitHub/HackUSU2025/CustomData/NILData/NILPower5.csv")

# List of P5 private schools as (school, conference) pairs
private = {
    'Duke': 'ACC',
    'Miami (FL)': 'ACC',
    'ND': 'ACC',
    'Boston College': 'ACC',
    'Wake Forest': 'ACC',
    'Syracuse': 'ACC',
    'Vanderbilt': 'SEC',
    'Stanford': 'ACC',
    'USC': 'Big Ten',
    'Northwestern': 'Big Ten',
    'Baylor': 'Big 12',
    'BYU': 'Big 12',
    'TCU': 'Big 12',
    'SMU': 'ACC'
}

# Dictionary for conference NIL averages increased by 15%
avgnil = {
    'ACC': 10946275,
    'Big 12': 11377377,
    'Big Ten': 11772392,
    'SEC': 14642200
}

# Add private schools to DataFrame
for school, conf in private.items():
    new_row = pd.DataFrame({
        'Collective Funding': [avgnil.get(conf, '-')],  # Use .get() to avoid key errors
        'Total Support': ['-'],
        'Ticket Sales': ['-'],
        'Contributions': ['-'],
        'Conf': [conf],
        'School': [school]
    })

    # Append new row
    nil = pd.concat([nil, new_row], ignore_index=True)

# Convert 'Collective Funding' to integer after removing '$' and ','
nil['Collective Funding'] = nil['Collective Funding'].astype(str).replace({'\$': '', ',': ''}, regex=True).astype(int)

# Save the updated DataFrame to a new CSV file
nil.to_csv("/Users/lukenichols/Documents/GitHub/HackUSU2025/CustomData/NILData/NILPower5_Updated.csv", index=False)


