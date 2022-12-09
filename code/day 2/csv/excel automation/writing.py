#pip install xlwt
import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
style = xlwt.easyxf('font: bold 1, color red;')
# Specifying column 
sheet1.write(0, 0, 'City', style) 
sheet1.write(1, 0, 'Hyderabad') 
sheet1.write(2, 0, 'Chennai') 
sheet1.write(3, 0, 'Pune') 
sheet1.write(4, 0, 'Delhi') 
wb.save('example.xls') 
#-------------------------------------
