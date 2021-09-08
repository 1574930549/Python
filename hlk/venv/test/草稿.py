# -*- coding: utf-8 -*-
# r"C:\Users\zlh\Desktop\test.xlsx"
import pandas as pd
from sqlalchemy import create_engine
import time
import xlrd
import openpyxl
data = xlrd.open_workbook(r"H:\32020101094000-4月.xls")#文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。
table = data.sheet_by_name("Sheet1")#通过名称获取
nrows = table.nrows  #获取该sheet中的有效行数
print(nrows)