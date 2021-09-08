# coding: utf-8
'''
编写程序实现文件读取
获取csv或txt大数据文件的内容
获取指定字节数的数据
文件指针定位
计算程序的执行时间为下一步优化提供依据
csv文件的格式化处理
写文件
使用Python标准模块pickle处理文件中的对象的读写
'''
import time, csv
t1 = time.time()
myFileRead = open(r'G:\代码\Python\大数据实验\dic.csv', 'r', newline='')  # 用空字符替代回车换行符
data = csv.reader(myFileRead, delimiter=',', quotechar='@')  
myFileWrite = open(r'G:\代码\Python\大数据实验\userdata.bin', 'a+', newline='')
# 以追加形式在原有文件末尾写入文件并且可读，如果文件不存在则创建文件
# w的方式是覆盖原来的文件，如果文件不存在则创建文件
'''
import pickle
datalist = [x for x in data]
pickle.dump(datalist, myFileWrite)
'''
datalist = [x for x in data]
for y in datalist:
    myFileWrite.write(str(y))
myFileWrite.close()
myFileRead.close()
t2 = time.time()
print('程序执行时间：', t2 - t1, " 秒")
