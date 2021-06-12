import numpy as np
import pandas as pd

# series
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array(my_list)
d = {'a':10,'b':20,'c':30}
print(pd.Series( data = my_list))
print(pd.Series(my_list,labels))

# Numpy array to pandas series
print(pd.Series(arr))

# Dic to panda series
print(pd.Series(d))

#Unsinf an index
ser1 = pd.Series([1,2,3,4], index = ['USA','GER','ITA','JAP'])
print(ser1)