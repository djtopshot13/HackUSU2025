# strip white spaces
import pandas as pd
df = pd.read_csv('NILGroupof5.csv')

df['Collective Funding *'] = df['Collective Funding *'].str.rstrip() #getting rid of trailing space
df.to_csv('NILGroupof5.csv', index=False)