
# Create a class that can be called to fix the formatting of the csv in this dir (sample.csv) and return it as a df. 
# BONUS: Return the data grouped in the best manner you see fit.

import pandas as pd

df = pd.read_csv ('sample.csv',index_col='ID')

#replace blank space with 0
df = df.fillna(0).to_string()

# applying groupby() function to
# group the data on team value.
# gk = df.groupby('Master')

# print the first entries
# in all the groups formed.

print(df)

# gk.first()