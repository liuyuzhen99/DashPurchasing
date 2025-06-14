import glob
import os
import openpyxl
import pandas as pd
import warnings
from openpyxl.styles import Font, PatternFill
from openpyxl.styles.colors import Color
import xlrd

df = pd.read_excel(r'C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\桌面\项目相关\Aydin purchasing requirement\Part Overview for Dashboard.xlsx', sheet_name='A6L e-tron')

print(range(len(df)))

for i in range(len(df)):
    print(i, df.iloc[i, 1])

