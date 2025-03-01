import pandas as pd
NIL = pd.read_csv('NIL.csv')

NIL['Collective Funding'] = NIL['Collective Funding'].str.rstrip()

NIL.to_csv('NIL.csv', index=False)
