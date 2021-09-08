import random
from random import randint


def sjs(n):
    people = list(range(1, n + 1))  # 建立一个1到n的列表
    for i in range(1, n+1):  # 循环
        p = randint(0, len(people) - 1)  # 求出第几号学生出列
        print('第',i,'为',people[p], '号')  # 输出
        # print('号学生出列***')  # 输出格式
        # print('----------')  # 输出格式
        del people[p]  # 出列的人在列表中删除


if __name__ == '__main__':
    sjs(9)  # 调用函数
