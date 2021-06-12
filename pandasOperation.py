import pandas as pd

df = pd.DataFrame({'col1' : [1,2,3,4],
                   'col2' : [444,555,666,444],
                   'col3' : ['abc','def','ghi','xyz']})

# column to array
Arr = df['col2'].unique()
# print(Arr)

# elements in specific column
Ele = df['col2'].nunique()
# print(Ele)

# frequency in specific column
Freq = df['col2'].value_counts()
# print(Freq)


# Selection data
newdf = df[ (df['col1'] > 2) & (df['col2'] == 444)]
# print(newdf)


# Applying with functions
def times2(x):
    return x*2
X2 = df['col1'].apply(times2)
# print(X2)

# Count Character
CountLen = df['col3'].apply(len)
# print(CountLen)


# Delete column permanetly
del df['col1'] # already delete
# print(df)

# Sorting Data
SortData = df.sort_values(by = 'col2')
# print(SortData)

# finding Nan
findNan = df.isnull()
# print(findNan)


# Odering Data
data = {'Place' : ['Hospital','School','University','PLStation','Stadium','Bar'],
        'Name' : ['Raksa','SWR','KMITL','Ladkrabang','KMITL','Society'],
        'Status' : ['open','open','close','open','close','close'],
        'Num' : [600,1000,10000,50,30,100]}

dict_DF = pd.DataFrame(data)
dfOrder = dict_DF.pivot_table(values='Num', index=['Place'], columns=['Status'],)
print(dfOrder)