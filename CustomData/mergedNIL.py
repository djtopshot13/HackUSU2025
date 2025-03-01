import pandas as pd
# Read the two CSV files
NIL = pd.read_csv('NIL.csv')
NILGroup = pd.read_csv('NILGroupof5.csv')

combined_df = pd.concat([NIL, NILGroup], ignore_index=True)

combined_df.to_csv('MergedNIL.csv', index=False)

