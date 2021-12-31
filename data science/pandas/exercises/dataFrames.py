# Data sets in pandas are usually multi-dimensional tables, called DataFrames
# Series is like a column, a Data Frame is the whole table
# A pandas Data Frame is a 2 dimensional data structure, like a 2 dimensional array, or table with rows and column

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
}

df = pd.DataFrame(data)
print(df)

# how to locate a row in a Data Frame
# Pandas use the loc attribute to return one or more specified rows(s) Note: This example returns a Pandas Series
print(df.loc[0])
print(df.loc[[0, 1]])       # when using [], the result is a pandas Data Frame

# named Indexes




