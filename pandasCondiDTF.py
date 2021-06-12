import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)

# Create Dataframe
df = pd.DataFrame(randn(5,4), index = 'A B C D E'.split(), columns = 'W X Y Z'.split())
print(df)

# # returning true or flase
# print(df > 0)
# # filter indexing
# print(df[ df > 0 ])
# print(df[df ['W'] > 0])

