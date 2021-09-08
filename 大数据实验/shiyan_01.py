#coding: utf-8
'''
编写程序实现文件读取
获取csv或txt大数据文件的内容
获取指定字节数的数据
文件指针定位
计算程序的执行时间为下一步优化提供依据
'''
import time
t1=time.time()
myFile=open(r'G:\代码\Python\大数据实验\dic.csv', 'r')
#s=myfile.read()
s=myFile.read(100000)
print(s)
t2=time.time()
print('程序执行时间：',t2-t1," 秒")
#打印输出dic.txt文件中内容的前100000个字节的内容