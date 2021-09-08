# ！/usr/bin/env python
# -*- coding：utf-8 -*-
# author: haotian time:2019/9/15

import numpy as np

f = open("./data/schedule_PlaneNum.csv", "rb")
result = open("./data/judge_result.csv", "w")
timedata = np.loadtxt(f, dtype=int, delimiter=",", skiprows=1, usecols=[12, 13])  # 分隔符 空格,


def judger():
    for i in range(len(timedata)):
        t1 = timedata[i][0]
        t3 = timedata[i][1]
        if t1 <= t3:
            print(str(i) + ',t1 <= t3 ###### the result is 遗传算法')
            # 排队的先到，那么肯定要接
            result.write(str(i) + ',遗传算法,\n')
        if t1 > t3:
            # 放空的先到
            t4 = t1 - t3
            # t/min = 平均每分钟一公里
            Wt3 = -0.6*(t3/60)  # 油费
            Wt4 =(1.9-0.6) * (t4/60)
            Wt = Wt4 + Wt3
            if Wt >= 0:
                print(str(i) + ",t1 > t3,Wt >= 0 ###### the result is 遗传算法")
                result.write(str(i) + ',遗传算法,\n')
            else :
                print(str(i) + ",t1 > t3,Wt < 0 ###### the result is 0")
                result.write(str(i) + ',0,\n')

judger()
result.close()