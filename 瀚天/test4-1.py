#!/usr/bin/env python3
# coding: utf-8
import xlrd

# 打开excel文件，创建一个workbook对象,book对象也就是fruits.xlsx文件,表含有sheet名
rbook = xlrd.open_workbook('kegg.xlsx')
# sheets方法返回对象列表,[<xlrd.sheet.Sheet object at 0x103f147f0>]
rbook.sheets()
# xls默认有3个工作簿,Sheet1,Sheet2,Sheet3
rsheet = rbook.sheet_by_index(0)  # 取第一个工作簿
Count=[]
Name=[]
# 循环工作簿的所有行
for row in rsheet.get_rows():
    count = row[2]  # 品名所在的列
    name = row[1]
    name = name.value  # 项目名
    Name.append(name)
    count = count.value  # 项目名
    Count.append(count)
# print(Name)
# print(Count)
del Name[0]
del Count[0]
# print(Name)
# print(Count)
for i in range(len(Count)):
    if int(Count[i])>20:
        print(Name[i])