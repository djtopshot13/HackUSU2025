import pandas as pd
NIL = pd.read_csv('NIL.csv')

NIL['Collective Funding'] = NIL['Collective Funding'].str.rstrip()
NIL['Conf'] = NIL['2024 Conference']
NIL = NIL.drop('2024 Conference', axis=1)

NIL.to_csv('NIL.csv', index=False)
# drop NIL2023 column
# regular NIL change 2024 conference to conf
