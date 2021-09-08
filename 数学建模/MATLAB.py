import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = '附件3-弹性模量与压力.xlsx'
data = pd.read_excel(data)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

y = data[u'压力(MPa)']
x = data[u'弹性模量(MPa)']

plt.plot(x, y, marker='.', markersize=0.1, label='实际的')
f = np.polyfit(x, y, 2)

k = f[0] * (x ** 2) + f[1] * x ** 1 + f[2]
plt.plot(x, k, label='模拟的')
print(f)

plt.ylabel('燃油密度(mm3/ms)')
plt.xlabel('压力(MPa)')
plt.title('压力与燃油密度的关系')
plt.legend()
plt.show()

C = 0.85  # 流量系数
A = math.pi * 0.7 ** 2  # 小孔的面积 遗传算法.539380374mm2
P2 = 160  # 高压油管端压力
P1 = 100  # 100MPa压力
rou160 = 0.868705986  # 高压油管端油气密度
rou = 0.85  # 100MPa油气密度

v0 = 500 * math.pi * 5 ** 2  # 高压油管体积
m = v0 * 0.85  # 高压油管油气质量
t = 0  # 开始时刻 t每增进1则进行0.01ms
P_list = []  # 压强时刻表


# 密度转压强
def P(n):
    return f[0] * (n ** 2) + f[1] * n ** 1 + f[2] - 1.6


# 进油函数 t1为进油时间段
def enter(t, t1):
    if 0 < t % (t1 + 10) < t1:
        global m
        global P1
        global rou
        Q1 = C * A * math.sqrt(2 * (P2 - P1) / rou160)  # 单位时间进油量
        det_m1 = Q1 * rou160 * 0.01  # 0.01为步长 质量改变量
        m = m + det_m1  # 更新质量
        rou = m / v0  # 更新密度
        P1 = P(rou)  # 更新压强
    else:
        pass


# 出油函数 t1为出油时间点
def out(t, t2):
    global rou
    global m
    global P1
    if t % 100 == t2:
        pass
    if t2 < (t % 100) < t2 + 0.2:
        Q2 = (t - t2) % 100 * 100
        det_m2 = Q2 * rou * 0.01  # 0.01为步长 质量改变量
        m = m - det_m2  # 更新质量
        rou = m / v0  # 更新密度
        P1 = P(rou)  # 更新压强
    elif t2 + 0.2 <= (t % 100) < t2 + 2.2:
        Q2 = 20
        det_m2 = Q2 * rou * 0.01  # 0.01为步长 质量改变量
        m = m - det_m2  # 更新质量
        rou = m / v0  # 更新密度
        P1 = P(rou)  # 更新压强
    elif t2 + 2.2 <= (t % 100) <= t2 + 2.4:
        Q2 = ((t - t2) * (-100) + 240) % 100
        det_m2 = Q2 * rou * 0.01  # 0.01为步长 质量改变量
        m = m - det_m2  # 更新质量
        rou = m / v0  # 更新密度
        P1 = P(rou)  # 更新压强
    else:
        pass


sum_min = 10000000000000  # 记录压力波动偏差最小值
P_real = []  # 记录压力最小时刻表
t_1 = 0  # 记录放气时间段
t_2 = 0  # 记录进气时间点

for i in np.arange(0.287, 0.288, 0.001):  # 遍历开阀门时间段 start->end
    for j in np.arange(52, 53, 1):  # 遍历出气时刻 start->end
        sum = 0  # 记录压力波动偏差
        t = 0
        P_list = []
        while (t <= 2000):  # 时间可修改，单位为ms
            t = t + 0.01
            enter(t, i)
            out(t, j)
            P_list.append(P1)
            sum = sum + abs(P1 - 100)
        print('i =', i, 'j =', j)
        print(sum)
        if sum_min > sum:
            sum_min = sum
            t_1 = i
            t_2 = j
            P_real = P_list

while (t <= 2000):  # 时间可修改，单位为ms
    t = t + 0.01
    enter(t, t_1)
    out(t, t_2)
    P_list.append(P1)

print(t_1, t_2)
x1 = np.arange(0, len(P_real) / 100, 0.01)
x2 = np.arange(0, len(P_real) / 100, 1000)
y_ = np.linspace(100,100,len(x2))
plt.xlabel('t(ms)')
plt.ylabel('P(KPa)')
plt.plot(x1, P_real, label='压强-时间')
plt.plot(x2, y_,marker='.',markersize=0.1)
plt.legend()
plt.show()