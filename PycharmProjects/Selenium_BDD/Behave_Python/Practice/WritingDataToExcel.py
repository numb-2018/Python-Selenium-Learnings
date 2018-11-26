import pandas as pd
import openpyxl

df1 = pd.DataFrame({'A': [1, 2, -3], 'B': [1, 2, 6]})
book = openpyxl.load_workbook('C:\\Users\\asingh\\PycharmProjects\\Selenium_BDD\\Behave_Python\\Practice\\ex1.xlsx') #Already existing workbook
writer = pd.ExcelWriter('C:\\Users\\asingh\\PycharmProjects\\Selenium_BDD\\Behave_Python\\Practice\\ex1.xlsx', engine='openpyxl') #Using openpyxl
#Migrating the already existing worksheets to writer
writer.book = book
writer.sheets = {x.title: x for x in book.worksheets}
df1.to_excel(writer, sheet_name='sheet4')
writer.save()
#reader = pd.read_excel('C:\\Users\\asingh\\PycharmProjects\\Selenium_BDD\\Behave_Python\\Practice\\ex1.xlsx', engine='openpyxl')
