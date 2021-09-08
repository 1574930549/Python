import numpy as np, pandas as pd

dataset = pd.read_excel(r"D:\XZ\test\test.xlsx")
dataset.head()
index = ["运单号码", "寄件日期", "收件姓名", "收件电话", "收件地址", "产品", "寄件姓名", "寄件电话", "寄件单位", "寄件地址", "重量", "应收费用"]
print(dataset.head())
print(dataset)
columns_names = dataset.columns.values.tolist()
print(columns_names[0])
for i in range(len(columns_names)):
    print(i)
    print(columns_names[i])
    columns_names[i]=index[i]
dataset.append(columns_names)
dataset.iloc[1,1]="运单号码"
# dataset.to_excel(r"D:\XZ\test\test.xlsx", index=False)
# df1 = pd.DataFrame({'Names': ['Andreas', 'George', 'Steve',
#                               'Sarah', 'Joanna', 'Hanna'],
#                     'Age': [21, 22, 20, 19, 18, 23]})
#
# df2 = pd.DataFrame({'Names': ['Pete', 'Jordan', 'Gustaf',
#                               'Sophie', 'Sally', 'Simone'],
#                     'Age': [22, 21, 19, 19, 29, 21]})
#
# df3 = pd.DataFrame({'Names': ['Ulrich', 'Donald', 'Jon',
#                               'Jessica', 'Elisabeth', 'Diana'],
#                     'Age': [21, 21, 20, 19, 19, 22]})
#
# dfs = {'Group1': df1, 'Group2': df2, 'Group3': df3}
# writer = pd.ExcelWriter('NamesAndAges.xlsx', engine='xlsxwriter')
#
# for sheet_name in dfs.keys():
#     dfs[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
#
# writer.save()
