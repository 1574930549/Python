import pandas as pd
from sqlalchemy import create_engine
import xlrd
import openpyxl as op
engine = create_engine("mysql+pymysql://root:1@3@localhost:3306/test")
con = engine.connect()  # 创建连接
# dataset=[1,2,3]
# dataset.to_sql(name='t_kdxx_all_2', con=con, if_exists='append', index=False)
str1=pd.read_sql('SELECT count(1) FROM test', con=engine, parse_dates=True)
print(str1)