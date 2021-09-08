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


plt.plot(x,y,marker='.', markersize=0.1,label='real')

f= np.polyfit(x,y,6)
y_=f[0]*x**6+f[1]*x**5+f[2]*x**4+f[3]*x**3+f[4]*x**2+f[5]*x+f[6]
print(f)

plt.plot(x,y_ ,label='fit')
plt.legend()
plt.show()



# 遗传算法.圆半径
def R(x):
    return f[0]*x**6+f[1]*x**5+f[2]*x**4+f[3]*x**3+f[4]*x**2+f[5]*x+f[6]
# 网页甘特图.圆心坐标
a, b = (0, 0)
# 参数方程
theta = np.arange(0, 2*np.pi, 0.01)
x = a + R(theta) * np.cos(theta)
y = b + R(theta) * np.sin(theta)
#绘图
plt.figure(figsize=(6,6))

plt.xlabel('x(mm)')
plt.ylabel('y(mm)')
plt.plot(x, y)
plt.show()