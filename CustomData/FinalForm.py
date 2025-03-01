# origin21%, origin22%, origin23%, destination21%, destination22%, destination23%
import pandas as pd

# Load the win-loss data for each year
cfb21 = pd.read_csv('CFBteam/clean_cfb21.csv')
cfb22 = pd.read_csv('CFBteam/clean_cfb22.csv')
cfb23 = pd.read_csv('CFBteam/clean_cfb23.csv')

# Calculate win percentage for each year
cfb21['win%'] = cfb21['wins'] / (cfb21['wins'] + cfb21['losses'])
cfb22['win%'] = cfb22['wins'] / (cfb22['wins'] + cfb22['losses'])
cfb23['win%'] = cfb23['wins'] / (cfb23['wins'] + cfb23['losses'])

# Create a dictionary to map team names to their win percentages for each year
win_percentages = {
    2021: cfb21.set_index('Team')['win%'].to_dict(),
    2022: cfb22.set_index('Team')['win%'].to_dict(),
    2023: cfb23.set_index('Team')['win%'].to_dict()
}

# Load the transfer portal data
portal_data = pd.read_csv('modified_CFB_Portal_Data.csv')

# Add win percentages to the portal data
portal_data['origin21%'] = portal_data['origin'].map(win_percentages[2021])
portal_data['origin22%'] = portal_data['origin'].map(win_percentages[2022])
portal_data['origin23%'] = portal_data['origin'].map(win_percentages[2023])
portal_data['destination21%'] = portal_data['destination'].map(win_percentages[2021])
portal_data['destination22%'] = portal_data['destination'].map(win_percentages[2022])
portal_data['destination23%'] = portal_data['destination'].map(win_percentages[2023])

# Save the modified portal data to a new CSV file
portal_data.to_csv('modified_CFB_Portal_Data.csv', index=False)