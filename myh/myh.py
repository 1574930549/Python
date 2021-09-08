import math
import xlwt
import pandas as pd
import openpyxl as op
f1 = open('./data_files-主生产计划/matinfo.dat', 'r') # 文件为123.txt
data1 = f1.read() # 按行读出文件内容
f1.close()
matinfo=[]
for i in data1.split():
    matinfo.append(i)
f2 = open('./data_files-主生产计划/order.dat', 'r') # 文件为123.txt
data2 = f2.read() # 按行读出文件内容
f2.close()
order=[]
for i in data2.split():
    order.append(i)
f3 = open('./data_files-主生产计划/period.dat', 'r') # 文件为123.txt
data3 = f3.read() # 按行读出文件内容
f3.close()
period=[]
for i in data3.split():
    period.append(i)
f4 = open('./data_files-主生产计划/prediction.dat', 'r') # 文件为123.txt
data4 = f4.read() # 按行读出文件内容
f4.close()
prediction=[]
for i in data4.split():
    prediction.append(i)
f5 = open('./data_files-主生产计划/PrevInventory.dat', 'r') # 文件为123.txt
data5 = f5.read() # 按行读出文件内容
f5.close()
PrevInventory=[]
for i in data5.split():
    PrevInventory.append(i)
f6 = open('./data_files-主生产计划/ScheduledReceipts.dat', 'r') # 文件为123.txt
data6 = f6.read() # 按行读出文件内容
f6.close()
ScheduledReceipts=[]
for i in data6.split():
    ScheduledReceipts.append(i)


print('matinfo',matinfo)
print('order',order)
print('period',period)
print('prediction',prediction)
print('PrevInventory',PrevInventory)
print('ScheduledReceipts',ScheduledReceipts)
wb = op.load_workbook("./data_files-主生产计划/新建 Microsoft Excel 工作表.xlsx")
sh = wb["Sheet1"]
for i in range(1,len(matinfo)+1):
    sh.cell(row=i, column=1, value=matinfo[i-1])
wb.save("./data_files-主生产计划/新建 Microsoft Excel 工作表.xlsx")