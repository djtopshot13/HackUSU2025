import pandas as pd
df = pd.read_csv('Total Group 5 Grades.csv')

df = df.drop(columns=['Rank', 'Unnamed: 1', 'Player GSIS', 'Player Sportradar Id'])

df.to_csv('Total Group 5 Grades.csv', index=False)