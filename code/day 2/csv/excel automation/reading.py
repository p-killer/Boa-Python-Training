#pip install xlrd
# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = (r"e:\data.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
print(sheet.cell_value(0, 0))  #NAME
print(sheet.cell_value(0, 1))   #SEMISTER
print(sheet.cell_value(0, 2))    # ROLLNO
print('-'*50)
#-------------------------------------

# Program to extract number of rows using Python 
print(sheet.cell_value(0, 0))
# Extracting number of rows 
print(sheet.nrows) # 5
print('-'*50)
#-------------------------------
# Program to extract number of columns in Python 
# For row 0 and column 0 
print(sheet.cell_value(0, 0))
# Extracting number of columns 
print(sheet.ncols)  #3
print('-'*50)
#------------------------------------
# Program extracting all columns  name in Python 
# For row 0 and column 0 
sheet.cell_value(0, 0) 
for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i)) 
print('-'*50)
#----------------------------------
# Program extracting first column 
for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 0))
print('-'*50)
#---------------------------------- 
#extract particular row value
print(sheet.row_values(1)) 
print('-'*50)
#----------------------------------