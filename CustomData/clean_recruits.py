import pandas as pd
df = pd.read_csv('CFB_Recruits_Data.csv')

df['committed_to'] = df['committed_to'].fillna('Not recruited out of HS') # if it was a null, they were not recruited out of HS, but maybe were later
df['school'] = df['school'].fillna('Not Listed') # too many mistakes- most of the ones I checked were recruited out of high school, it just wasn't listed
df['ranking'] = df['ranking'].fillna('Not Ranked') #assuming if there is no value they aren't ranked
df['country'] = df['country'].fillna('Not Listed') # not enough time to clean all the way- some are US, some are other countries
# lots of other missing values still: position, weight, height, city, state/province, athlete ID, 
df = df[~df['Unnamed: 0'].isin([9109, 350, 156, 660, 659, 748, 904, 976, 14288,14289, 14284])]
# # used this code to find duplicates based on these columns
# duplicate_rows = df[df.duplicated(subset=columns_to_check, keep=False)]
# print(duplicate_rows)

df.to_csv('CFB_Recruits_Data.csv', index=False)