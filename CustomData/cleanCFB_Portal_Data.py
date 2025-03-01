import pandas as pd
portal = pd.read_csv('CFB_Portal_Data.csv')

portal['stars'] = portal['stars'].fillna(0.0) # filling nulls with zeros
portal['destination'] = portal['destination'].fillna('none') #filling NA with none 
portal['rating'] = portal['rating'].fillna('None') # filling NA with none

print(portal.info()) # checking to see if I fixed all nulls 

portal.to_csv('CFB_Portal_Data.csv', index=False)

# # used this code to check if players are listed in the portal multiple times
# name_counts = portal.groupby(['first_name', 'last_name']).size().reset_index(name='count')
# name_counts = name_counts.sort_values(by='count', ascending=False) 
# print(name_counts)