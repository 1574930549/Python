# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import time
import xlrd
import openpyxl
wb = openpyxl.load_workbook(r"C:\Users\zlh\Desktop\test2.xlsx")#打开 Excel 文档
sheet1 = wb['Sheet1']
row_num = sheet1.max_row     # 获取当前表中最大的行数
for row in range(1, row_num+1):
    cell = sheet1.cell(row, 1)
    str1=str(cell.value)
    print(str1)
    str2=str1.replace("\\","\\\\").replace("./",'')
    print(str2)
    str3="H:\\\\"+str2
    print(str3)
    wb2=openpyxl.load_workbook(str3)
    sheet2 = wb2['Sheet1']
    column_num=sheet2.max_column
    print(column)
# H:\

