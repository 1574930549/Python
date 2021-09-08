# coding: utf-8
'''
编写程序实现文件读取
获取csv或txt大数据文件的内容
获取指定字节数的数据
文件指针定位
计算程序的执行时间为下一步优化提供依据
csv文件的格式化处理
'''
import time, csv
t1 = time.time()
myFile = open(r'G:\代码\Python\大数据实验\dic.csv', 'r', newline='')  # 用空字符替代回车换行符
# s=myfile.read()
data = csv.reader(myFile, delimiter=',', quotechar='|')  # 读取csv文件中的数据
# 通过设置 delimiter 和 quotechar 来配置分隔符和引用符常用于输出数据的格式化
# csv.reader(csvfile, dialect='excel', **fmtparams) 
# 例子：spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# Return a reader object which will iterate over lines in the given csvfile. 
# 所以这里的data变量是一个reader对象
'''
def read(file_location):
    with open(file_location, 'r+', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        return [row for row in reader]


def write(file_location, rows):
    with open(file_location, 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=' ', quotechar='|')
        for row in rows:
            writer.writerow(row)
'''
print(data)
# 直接打印输出data会得到一个内存地址
t2 = time.time()
print('程序执行时间：', t2 - t1, " 秒")
# 打印输出reader对象-data的内存地址并计算程序执行时间
