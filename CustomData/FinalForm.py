# origin21%, origin22%, origin23%, destination21%, destination22%, destination23%
import pandas as pd

# Load the win-loss data for each year
cfb21 = pd.read_csv('CFBteam/clean_cfb21.csv')
cfb22 = pd.read_csv('CFBteam/clean_cfb22.csv')
cfb23 = pd.read_csv('CFBteam/clean_cfb23.csv')

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
portal_data = pd.read_csv('RecruitsAndPortalData/modified_CFB_Portal_Data.csv')

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

# Save the modified portal data to a new CSV file
portal_data.to_csv('finalData.csv', index=False)