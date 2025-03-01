import pandas as pd
PFF = pd.read_csv('Power 5 Data/Power 5 Offense Grades.csv')
sum = 0
for index, row in PFF.iterrows():
    if row['Team'] == "TEXAS":
        sum  += row['OFF%'] * row['OFF']
print(sum)
print(max(PFF["OFF%"]) * 10000)