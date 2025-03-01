import pandas as pd
portal_df = pd.read_csv('RecruitsAndPortalData/modified_CFB_Portal_Data.csv')
NIL_df = pd.read_csv('NILData/NIL.csv')
merged_df = portal_df
# Merge on 'school' to bring in 'collective_funding'
# merged_df = portal_df.merge(NIL_df, left_on='origin', right_on='School', how='left')
# # Fill missing values in 'originNIL' using 'collective_funding'
# merged_df['originNIL'] = merged_df['originNIL'].fillna(merged_df['Collective Funding'])
# # Drop the extra 'collective_funding' column (we've already used it)
# merged_df = merged_df.drop(columns=['Collective Funding'])
# merged_df = portal_df.drop(columns=['destinationNIL', 'Ticket Sales', 'Ticket Sales_x', 'Ticket Sales_y', 'Total Support', 'Total Support_x', 'Total Support_y', 'Contributions', 'Contributions_x', 'Contributions_y', 'Conf', 'Conf_x', 'Conf_y', 'School', 'School_x', 'School_y'])
# merged_df['destination'] = merged_df['destination'].str.strip()
merged_df = portal_df
# merged_df.insert(loc=8, column='destinationNIL', value="No Data")

# Create dictionary from NIL_df
# school_to_nil = NIL_df.set_index('School')['Collective Funding'].to_dict()
# school_to_nil["none"] = "none"


# Map NIL values directly into merged_df
# merged_df['destinationNIL'] = merged_df['destination'].map(school_to_nil)
# merged_df['destinationNIL'] = merged_df['destinationNIL'].fillna("").replace("", "No Data")
merged_df['originNIL'] = merged_df['originNIL'].fillna("").replace("", "No Data")
# print(merged_df)
# print(merged_df.info())
# merged_df.drop(columns=['destinationNIL'], inplace=True)

merged_df.to_csv('RecruitsAndPortalData/modified_CFB_Portal_Data.csv', index=False)

