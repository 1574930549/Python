import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
data = '附件1-凸轮边缘曲线.xlsx'
data = pd.read_excel(data)

y = data[u'极径（mm）']
x = data[u'极角（rad）']

f = np.polyfit(x, y, 6)  # 六次函数拟合


def R(x):  # 极径 #x为极角 弧度制
    return f[0] * x ** 6 + f[1] * x ** 5 + f[2] * x ** 4 + f[3] * x ** 3 + f[4] * x ** 2 + f[5] * x + f[6]


w = 0.027  # 弧度制下的角速度
T = 2 * math.pi / w
y_max = []

for j in np.arange(117, T + 117, 1):  # 时间遍历，以周期为遍历end结束点
    ymax = 0  # 更新最大值
    for i in np.arange(0, 2 * math.pi, 0.01):  # 弧度制遍历
        y_point = R(i) * math.cos(w * j + i)  # 每一时间点下不同弧度坐标位置 y_point y坐标
        if y_point > ymax:
            ymax = y_point  # 每次遍历下来求得每一时间点下 不同弧度纵坐标最大值
    y_max.append(ymax)  # 将此时刻最大值添加到列表中

x = np.arange(0, len(y_max), 1)
plt.plot(x, y_max, label='活塞底部在y轴上的位置')
plt.xlabel('t/ms')
plt.ylabel('ymax/mm')
plt.legend()
plt.show()

x__ = np.arange(0, len(y_max), 1)  # 时间变量
vy = -w * R(0) * np.sin(2 * math.pi - w * x__)  # 速度变化

plt.plot(x__, vy, label='活塞速度')
plt.xlabel('t/ms')
plt.ylabel('v/mm')
plt.legend()
plt.show()

print(min(y_max), max(y_max), max(y_max) - min(y_max))  # 网页甘特图.4157081016847566 7.247512164299576 自动弹出网页甘特图.83180406261482