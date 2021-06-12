import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)

# Create Dataframe
df = pd.DataFrame(randn(5,4), index = 'A B C D E'.split(), columns = 'W X Y Z'.split())
print(df)

# Selection and Indexing Dataframe

# selection (only columns)
print(df[['W']])
print(df.W)

# removing columns
# axis 1 for columns, 0 for rows
print(df.drop('Z', axis = 1)) # remove in ideal
df.drop('Z', axis = 1, inplace = True) # real remove
print(df)
df.drop('A', axis = 0, inplace = True)
print(df)

print(df.loc['C', 'Y']) # loc row and cloumn
# .iloc use for indexing
print(df.iloc[2])

# Conditions Dataframe