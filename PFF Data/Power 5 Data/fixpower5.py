import pandas as pd
df = pd.read_csv('Power 5 ST Grades.csv')

df = df.drop(columns=['Rank', 'Unnamed: 1', 'Player GSIS', 'Player Sportradar Id'])

df.to_csv('Power 5 ST Grades.csv', index=False)