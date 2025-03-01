import pandas as pd

pfftest = pd.read_csv("/Users/lukenichols/Documents/GitHub/HackUSU2025/PFF Data/MW Data/pff-data.csv")

mwwinloss = {'BOISE ST': 12/14,
          'UNLV': 11/14,
          'COLO STATE': 8/13,
          'FRESNO ST': 6/13,
          'S JOSE ST': 7/13,
          'NEW MEXICO': 5/12,
          'HAWAII': 5/12,
          'UTAH ST': 4/12,
          'AIR FORCE': 5/12,
          'S DIEGO ST': 3/12,
          'WYOMING': 3/12,
          'NEVADA': 3/13}

# Add a new column for win percentages by mapping the teams
pfftest['win_percentage'] = pfftest['Team'].map(mwwinloss)

# Display the updated DataFrame
pfftest.to_csv("/Users/lukenichols/Documents/GitHub/HackUSU2025/PFF Data/MW Data/pff-data_updated.csv", index=False)