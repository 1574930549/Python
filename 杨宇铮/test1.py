import math
import matplotlib.pyplot as plt
import numpy as np
p=math.pi
# print(p)
R=6371393
z=(170*180)/(p*R)
# print(z)
N=48.980994
E=-122.688503

a = np.linspace(0, 100, 50) # 从0到1，等分50分
print(a)
# b = math.sqrt(30-(((a-N)*p*R/180)*((a-N)*p*R/180))*180/(p*R))+E # 这里是函数的表达式
b=a
plt.figure() # 定义一个图像窗口
plt.plot(a, b) # 绘制曲线 y

plt.show()