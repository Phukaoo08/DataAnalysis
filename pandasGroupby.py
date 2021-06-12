import pandas as pd

# Dict key and value (Basic)
data = {'Company' : ['SCG','PTT','KTB','SEA','QUA','IMP'],
        'Person'  : ['Mr.A','Mr.B','Mr.C','Mr.D','Mr.E','Mr.F'],
        'Sales'   : [200,120,340,124,243,350]}

# change Dict to dataframe
df = pd.DataFrame(data)
print(df)

newData = {'Company' : ['SCG','PTT','PTT','SEA','SCG','SEA'],
           'Person'  : ['Mr.A','Mr.B','Mr.C','Mr.D','Mr.E','Mr.F'],
           'Sales'   : [200,120,340,124,243,350]}

dfNew = pd.DataFrame(newData)
print('\n')

# Grouping by company
by_company = dfNew.groupby('Company') # create 'groupBy' variable 
print(by_company.mean()) # show all companies and mean in each companies
print('\n')
print(by_company.std()) # show all companies and std in each companies
print('\n')

# Show all statistic by pandas
print(by_company.describe())
print('\n')

# Transpoes a matrix of dataframe
print(by_company.describe().transpose())
print('\n')

# chosing a specific company
print(by_company.describe().transpose()['PTT'])