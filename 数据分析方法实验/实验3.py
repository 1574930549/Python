import numpy
import random
import codecs
import copy
import re
import matplotlib.pyplot as plt
import xlrd
import pandas as pd
import numpy as np


def calcuDistance(vec1, vec2):
    # 计算向量vec1和向量vec2之间的欧氏距离
    return numpy.sqrt(numpy.sum(numpy.square(vec1 - vec2)))


def loadDataSet(fileName): # 读数据，np实现
    data = pd.read_excel(fileName)
    # print(type(data))
    train_data = np.array(data)  # np.ndarray()
    dataMat = train_data.tolist()  # list

    print(dataMat)

    return dataMat


# def loadDataSet(fileName): # 读数据，不用np实现
#     data1 = xlrd.open_workbook(fileName)
#     sheet1 = data1.sheet_names()
#     table1 = data1.sheet_by_name(sheet1[0])
#     Alcohol = table1.col_values(1)
#     del Alcohol[0]
#     Mali_cacid = table1.col_values(2)
#     del Mali_cacid[0]
#     Ash = table1.col_values(3)
#     del Ash[0]
#     Alcalinity_of_ash = table1.col_values(4)
#     del Alcalinity_of_ash[0]
#     Magnesium = table1.col_values(5)
#     del Magnesium[0]
#     Total_phenols = table1.col_values(6)
#     del Total_phenols[0]
#     Flavanoids = table1.col_values(7)
#     del Flavanoids[0]
#     dataMat = [[0 for i in range(7)] for i in range(len(Alcohol))]
#     for i in range(len(Mali_cacid)):
#         dataMat[i][0] = Alcohol[i]
#         dataMat[i][1] = Mali_cacid[i]
#         dataMat[i][2] = Ash[i]
#         dataMat[i][3] = Alcalinity_of_ash[i]
#         dataMat[i][4] = Magnesium[i]
#         dataMat[i][5] = Total_phenols[i]
#         dataMat[i][6] = Flavanoids[i]
#     return dataMat


def initCentroids(dataSet, k):
    # 初始化k个质心，随机获取
    return random.sample(dataSet, k)  # 从dataSet中随机获取k个数据项返回


def minDistance(dataSet, centroidList):
    # 对每个属于dataSet的item，计算item与centroidList中k个质心的欧式距离，找出距离最小的，
    # 并将item加入相应的簇类中

    clusterDict = dict()  # 用dict来保存簇类结果
    for item in dataSet:
        vec1 = numpy.array(item)  # 转换成array形式
        flag = 0  # 簇分类标记，记录与相应簇距离最近的那个簇
        minDis = float("inf")  # 初始化为最大值

        for i in range(len(centroidList)):
            vec2 = numpy.array(centroidList[i])
            distance = calcuDistance(vec1, vec2)  # 计算相应的欧式距离
            if distance < minDis:
                minDis = distance
                flag = i  # 循环结束时，flag保存的是与当前item距离最近的那个簇标记

        if flag not in clusterDict.keys():  # 簇标记不存在，进行初始化
            clusterDict[flag] = list()
            # print flag, item
        clusterDict[flag].append(item)  # 加入相应的类别中

    return clusterDict  # 返回新的聚类结果


def getCentroids(clusterDict):
    # 得到k个质心
    centroidList = list()
    for key in clusterDict.keys():
        centroid = numpy.mean(numpy.array(clusterDict[key]), axis=0)  # 计算每列的均值，即找到质心
        # print key, centroid
        centroidList.append(centroid)

    return numpy.array(centroidList).tolist()


def getVar(clusterDict, centroidList):
    # 计算簇集合间的均方误差
    # 将簇类中各个向量与质心的距离进行累加求和

    sum = 0.0
    for key in clusterDict.keys():
        vec1 = numpy.array(centroidList[key])
        distance = 0.0
        for item in clusterDict[key]:
            vec2 = numpy.array(item)
            distance += calcuDistance(vec1, vec2)
        sum += distance

    return sum


def showCluster(centroidList, clusterDict, x, y):
    # 展示聚类结果

    colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow']  # 不同簇类的标记 'or' --> 'o'代表圆，'r'代表red，'b':blue
    centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw']  # 质心标记 同上'd'代表棱形
    for key in clusterDict.keys():
        plt.plot(centroidList[key][x], centroidList[key][y], centroidMark[key], markersize=12)  # 画质心点
        for item in clusterDict[key]:
            # print(item[0], item[1])
            plt.plot(item[x], item[y], colorMark[key])  # 画簇类下的点

    plt.show()


def run(centroidList, clusterDict, newVar):
    x = 1
    y = 2
    oldVar = -0.0001  # 旧均方误差值初始化为-1
    print('***** 第1次迭代 *****')
    print('簇类')
    for key in clusterDict.keys():
        print(key, ' --> ', clusterDict[key])
    print('k个均值向量: ', centroidList)
    print('平均均方误差: ', newVar)
    showCluster(centroidList, clusterDict, x, y)  # 展示聚类结果

    k = 2
    while abs(newVar - oldVar) >= 0.0001:  # 当连续两次聚类结果小于0.0001时，迭代结束
        centroidList = getCentroids(clusterDict)  # 获得新的质心
        clusterDict = minDistance(dataSet, centroidList)  # 新的聚类结果
        oldVar = newVar
        newVar = getVar(clusterDict, centroidList)

        print('***** 第%d次迭代 *****' % k)
        print('簇类')
        for key in clusterDict.keys():
            print(key, ' --> ', clusterDict[key])
        print('k个均值向量: ', centroidList)
        print('平均均方误差: ', newVar)
        showCluster(centroidList, clusterDict, x, y)  # 展示聚类结果
        k += 1


if __name__ == '__main__':
    inFile = r"C:\Users\zlh\Desktop\数据分析方法实验\实验三、四\wine.xlsx"  # 数据集文件
    dataSet = loadDataSet(inFile)  # 载入数据集
    centroidList = initCentroids(dataSet, 3)  # 初始化质心，设置k=4
    clusterDict = minDistance(dataSet, centroidList)  # 第一次聚类迭代
    newVar = getVar(clusterDict, centroidList)  # 获得均方误差值，通过新旧均方误差来获得迭代终止条件
    run(centroidList, clusterDict, newVar)
