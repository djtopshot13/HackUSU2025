import pandas as pd

pfftest = pd.read_csv("PFF Data/MW Data/pff-data.csv")

mwwinloss = {'BOISE ST': round(12/14, 2),
          'UNLV': round(11/14, 2),
          'COLO STATE': round(8/13, 2),
          'FRESNO ST': round(6/13, 2),
          'S JOSE ST': round(7/13, 2),
          'NEW MEXICO': round(5/12, 2),
          'HAWAII': round(5/12, 2),
          'UTAH ST': round(4/12, 2),
          'AIR FORCE': round(5/12, 2),
          'S DIEGO ST': round(3/12, 2),
          'WYOMING': round(3/12, 2),
          'NEVADA': round(3/13, 2)}

# Add a new column for win percentages by mapping the teams
pfftest['origin24%'] = pfftest['Team'].map(mwwinloss)

# Display the updated DataFrame


import pandas as pd

# Load the win-loss data for each year
cfb21 = pd.read_csv('CustomData/CFBteam/clean_cfb21.csv')
cfb22 = pd.read_csv('CustomData/CFBteam/clean_cfb22.csv')
cfb23 = pd.read_csv('CustomData/CFBteam/clean_cfb23.csv')

# Calculate win percentage for each year
cfb21['win%'] = round(cfb21['Win'] / cfb21['Games'], 2) * 100
cfb22['win%'] = round(cfb22['Win'] / cfb22['Games'], 2) * 100
cfb23['win%'] = round(cfb23['Win'] / cfb23['Games'], 2) * 100

# Create a dictionary to map team names to their win percentages for each year
win_percentages = {
    2021: cfb21.set_index('Team')['win%'].to_dict(),
    2022: cfb22.set_index('Team')['win%'].to_dict(),
    2023: cfb23.set_index('Team')['win%'].to_dict() 
}

# Load the transfer portal data
portal_data = pd.read_csv('CustomData/RecruitsAndPortalData/modified_CFB_Portal_Data.csv')

# Add win percentages to the portal data
portal_data['origin21%'] = portal_data['origin'].map(win_percentages[2021])
portal_data['origin22%'] = portal_data['origin'].map(win_percentages[2022])
portal_data['origin23%'] = portal_data['origin'].map(win_percentages[2023])
portal_data['destination21%'] = portal_data['destination'].map(win_percentages[2021])
portal_data['destination22%'] = portal_data['destination'].map(win_percentages[2022])
portal_data['destination23%'] = portal_data['destination'].map(win_percentages[2023])

o21 = portal_data.pop('origin21%')
o22 = portal_data.pop('origin22%')
o23 = portal_data.pop('origin23%')
d21 = portal_data.pop('destination21%')
d22 = portal_data.pop('destination22%')
d23 = portal_data.pop('destination23%')
portal_data.insert(loc=6, column='origin21%', value=o21)
portal_data.insert(loc=7, column='origin22%', value=o22)
portal_data.insert(loc=8, column='origin23%', value=o23)
portal_data.insert(loc=11, column='destination21%', value=d21)
portal_data.insert(loc=12, column='destination22%', value=d22)
portal_data.insert(loc=13, column='destination23%', value=d23)


filtered_data = portal_data[(portal_data['origin'].isin(list(mwwinloss.keys()))) | (portal_data['destination'].isin(list(mwwinloss.keys())))]
o24 = pfftest.pop("origin24%")
filtered_data.insert(loc=9, column='origin24%', value=o24)
# Save the modified portal data to a new CSV file
filtered_data['origin21%'] = filtered_data["origin21%"].fillna("-")
filtered_data.to_csv('PFF Data/MW Data/pff-data_updated.csv', index=False)

