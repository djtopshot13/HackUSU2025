# strip white spaces
import pandas as pd
df = pd.read_csv('NILGroupof5.csv')

df['Collective Funding'] = df['Collective Funding *'] #renaming column for joining purposes
df = df.drop('Collective Funding *', axis=1)

df.to_csv('NILGroupof5.csv', index=False)