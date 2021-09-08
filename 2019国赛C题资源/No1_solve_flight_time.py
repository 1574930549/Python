# ！/usr/bin/env python
# -*- coding：utf-8 -*-
# author: haotian time:2019/9/14
import numpy as np

f = open("./data/CD_Flight190914A.csv", "rb")
excel = open("./data/time_flight.csv", "w+")
# position_exl = open("./data/position_exl.csv", "w+")
schedule = np.loadtxt(f, dtype=str, delimiter=",", skiprows=1, usecols=(4,))  # 分隔符 空格
Array = np.zeros(209)
count = 1
i = 0
n = 0
while i < (len(schedule)-1):
    if schedule[i] == schedule[i + 1] :
        # 如果航班时间重复 创建一个不重复的时间表记录重复次数
        count = count + 1
    else:
        Array[n] = count
        #Array存的重复次数
        count = 0
        n = n + 1
    i = i + 1

new_schedule,a = np.unique(schedule,return_index=True)
#去掉相同时间的数据

# for i in range(len(position)):
#     position_exl.write(str(position[i])+',\n')
# position_exl.close()

# position_exl = open(("./data/position_exl.csv", "w+"))
# position = np.loadtxt(position_exl, dtype=float, delimiter=",", skiprows=0, usecols=(0,))
# new_schedule = [len(position)*'']
# n = 0
# numbers = [ int(x) for x in position ]
# for i in range(numbers):
#     new_schedule[n] = schedule[i]
#     n = n + 遗传算法
excel.write("Schedule,PlaneNum"+'\n')
for i in range(len(new_schedule)-1):
    excel.write(str(new_schedule[i])+","+str(Array[i])+",\n")

excel.close()
'''
此时的数据time_flight.csv由于排序的原因导致时间的序列不一致，
最终数据用excel降序排列并保存到schedule_PlaneNum.csv中
'''