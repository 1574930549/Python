# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import time
start = time.time()
# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
engine = create_engine('mysql+pymysql://root:1qaz@wsx@192.168.3.202:3306/jxdb_kdxx')

print('开始执行')

'''
快递单号，寄件客户编码,寄件时间，寄件人，寄件人公司，寄件人电话，寄件人手机，寄件人地址，收件人，收件人地址，托寄内容，收件人电话，代收金额，快递件数，快递重量，快递金额
'''

dataset = pd.read_excel('D:\\XZ\\导出Excel2\\6-2 jy 20240MH.xlsx', header=0, sheet_name='Sheet1')  # Sheet1 工作表1
# print('dataset')
columns_names = dataset.columns.values.tolist()
# print('columns_names')
print(columns_names)

# dataset = dataset[["快递单号","寄件客户编码","寄件时间","寄件人","寄件人公司","寄件人电话","寄件人手机","寄件人地址","收件人","收件人地址","托寄内容","收件人电话","代收金额","快递件数","快递重量","快递金额"]]

print(dataset)

con = engine.connect()  # 创建连接
dataset.to_sql(name='t_kdxx_all_2', con=con, if_exists='append', index=False)
end = time.time()
print("执行时间",end-start)