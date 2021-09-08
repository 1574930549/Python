# -*- coding: utf-8 -*-
# r"C:\Users\zlh\Desktop\test.xlsx"
import pandas as pd
from sqlalchemy import create_engine
import time
import xlrd
import openpyxl
wb2=openpyxl.load_workbook("H:\\10-27乐拍16403 蜂胶 酒都选了.xlsx")
sheet2 = wb2['Sheet1']
column_num=sheet2.max_column