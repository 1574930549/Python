#coding: utf-8
'''
编写程序实现文件读取
获取csv或txt大数据文件的内容
获取指定字节数的数据
文件指针定位
计算程序的执行时间为下一步优化提供依据
'''
myFile=open(r'G:\代码\Python\大数据实验\dic.txt', 'r')
s=myFile.read(1000000)
print(s)
#注释和取消注释的快捷键Ctrl+/
myFile.seek(0)      #文件指针回到文件开头
s=myFile.read(29)   #再重新从文件头开始读29个字节并打印输出
print(s)