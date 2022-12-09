#pip install xlrd                for excel support
import pandas as pd
import numpy as np
df = pd.read_excel("salesdata.xlsx")
print(df.head())

#pivot table with
sales_report = pd.pivot_table(df, index=["Manager", "Rep", "Product"], values=["Price", "Quantity"],
                           aggfunc=[np.sum, np.mean], fill_value=0)
print(sales_report.head())
