import xlrd

wb = xlrd.open_workbook("C://Users//asingh//Desktop//DataExcel.xlsx")
print(wb.sheet_names())
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(1, 1))
print("Number of rows {0} in the excel is  ".format(sheet.cell_value(1, 3)))

