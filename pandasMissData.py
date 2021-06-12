import numpy as np
import pandas as pd

# Dict to Dataframe
df = pd.DataFrame({'A' : [1,2,np.nan],'B' : [5,np.nan,np.nan],'C' : [1,2,3]})

# Nan is an example for missing Data in Dataframe
# print(df)

# Collecting a completely matrix axis 0 = row ,axis 1 = column ,none axis = default(row and column)
print(df.dropna(axis = 0))
print('\n')
print(df.dropna(axis = 1))
print('\n')

# threshold accept atlesat 'n' Nan data
#if thresh = 2 then data can have only 1 Nan value
print(df.dropna(thresh = 2))
print('\n')

# change Nan to another word
df.fillna( value = 'Error',inplace = True)
print(df)
