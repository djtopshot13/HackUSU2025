import pandas as pd
portal_df = pd.read_csv('RecruitsAndPortalData/modified_CFB_Portal_Data.csv')
NIL_df = pd.read_csv('NILData/NIL.csv')

# Merge on 'school' to bring in 'collective_funding'
merged_df = portal_df.merge(NIL_df, left_on='origin', right_on='School', how='left')
# Fill missing values in 'originNIL' using 'collective_funding'
merged_df['originNIL'] = merged_df['originNIL'].fillna(merged_df['Collective Funding'])
# Drop the extra 'collective_funding' column (we've already used it)
merged_df = merged_df.drop(columns=['Collective Funding'])

# Create dictionary from NIL_df
school_to_nil = NIL_df.set_index('School')['Collective Funding'].to_dict()

# Map NIL values directly into merged_df
merged_df['destinationNIL'] = merged_df['destination'].map(school_to_nil)

print(merged_df)
# print(merged_df.info())

# merged_df.to_csv('RecruitsAndPortalData/modified_CFB_Portal_Data.csv', index=False)

