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
# merged_df.insert(loc=8, column='destinationNIL', value="No Data")
# NIL_df['School'] = NIL_df['School'].fillna("UT San Antonio").replace("Texas at San Antonio", "UTSA")
# merged_df['destination'] = merged_df['destination'].fillna("UT San Antonio").replace("UT San Antonio", "UTSA")
# merged_df['origin'] = merged_df['origin'].fillna("UT San Antonio").replace("UT San Antonio", "UTSA")
# merged_df['destination'] = merged_df['destination'].fillna("Alabama at Birmingham").replace("Alabama at Birmingham", "UAB")
# merged_df['origin'] = merged_df['origin'].fillna("Alabama at Birmingham").replace("Alabama at Birmingham", "UAB")
# NIL_df['School'] = NIL_df['School'].fillna("Alabama at Birmingham").replace("Alabama at Birmingham", "UAB")
# NIL_df['School'] = NIL_df['School'].fillna("Hawaii (Football)").replace("Hawaii (Football)", "Hawaii")
# NIL_df['School'] = NIL_df['School'].fillna("Louisiana - Lafayette").replace("Louisiana - Lafayette", "Louisiana")
# NIL_df['School'] = NIL_df['School'].fillna("Louisiana - Monroe").replace("Louisiana - Monroe", "Louisiana Monroe")
# Create dictionary from NIL_df
school_to_nil = NIL_df.set_index('School')['Collective Funding'].to_dict()
school_to_nil["none"] = "none"


# Map NIL values directly into merged_df
merged_df['destinationNIL'] = merged_df['destination'].map(school_to_nil)
merged_df['originNIL'] = merged_df['origin'].map(school_to_nil)

# merged_df['originNIL'] = merged_df['originNIL'].fillna("").replace("", "No Data")
# print(merged_df)
# print(merged_df.info())
# merged_df.drop(columns=['destinationNIL'], inplace=True)
# NIL_df.to_csv('NILData/NIL.csv', index=False)
merged_df.to_csv('RecruitsAndPortalData/modified_CFB_Portal_Data.csv', index=False)

