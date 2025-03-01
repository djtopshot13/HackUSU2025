import pandas as pd
NIL = pd.read_csv('NIL.csv')

NIL['School'] = NIL['Public Universities']
NIL = NIL.drop('Public Universities', axis=1)

NIL.to_csv('NIL.csv', index=False)
# drop NIL2023 column
# regular NIL change 2024 conference to conf
