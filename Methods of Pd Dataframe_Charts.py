
>>>>>> Method 1: How to Import an Excel File into Python using Pandas::

import pandas as pd

df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx')
print (df)



>>>>> Method 2: And if you have a specific Excel sheet that you like to import ::

import pandas as pd
df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx', sheet_name='your Excel sheet name')
print (df)
