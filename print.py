
import csv
myFile = open(r'G:\代码\Python\大数据实验\dic.csv')  # 用空字符替代回车换行符
data = myFile.readlines()
print(data,sep=',')
myFile.close()