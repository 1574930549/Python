#！/usr/bin/env python
# -*- coding：utf-8 -*-
# author: haotian time:2019/9/15
import os  # 创建文件夹需要用
import numpy as np
f = open("./data/distribute_2016.08.08_510100_.csv", "rb")
schedule = np.loadtxt(f, dtype=str, delimiter=",", skiprows=1)  # 分隔符 空格

def exl_download(n, address):
    os.makedirs('./' + str(address) + '/', exist_ok=True)
    for a in range(n):
        print('No' + str(a) + 'exl is downloading')
        with open('./' + str(address) + '/' + str(a) + '.csv', 'w') as f1:
            for i in range(len(schedule)-1):
                if(schedule[i][1]==str(a)):
                    for j in range(5):
                        print('Writing......')
                        schedule[i][j].encode("utf-8")
                        f1.write(schedule[i][j]+',')
                    f1.write('\n')
        f1.close()
        print('No' + str(a) + 'exl is downloaded')
exl_download(24, 'distribute')


