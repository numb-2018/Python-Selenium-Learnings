import pandas as pd

# Read the excel (Get the reference of excel)
df = pd.read_excel("C://Users//asingh//PycharmProjects//Selenium_BDD//Behave_Python//Practice//DataExcel.xlsx",
                   sheet_name="UserCredentials")
print("Column headings:")
print('Column count => {0}'.format(len(df.columns)))
print("Column headings:")
print('Row count => {0}'.format(len(df.index)))
print('****************************')
print('Row count 1 => {0}', df.all())
print('****************************\n')
print('Row count 2 => {2}')
print('****************************\n')


print(df['UserName'][2])
print(df['Password'][2])
print(df['Description'][2])
print('****************************\n')

# Loop to get all data
for i in df.index:
    print(df['UserName'][i])
    print(df['Password'][i])
    print(df['Description'][i])
