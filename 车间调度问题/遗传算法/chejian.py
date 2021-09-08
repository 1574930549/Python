import numpy as np
import matplotlib.pyplot as plt
import random
import itertools

GSP = 0.6  # 全局选择的GS概率
LSP = 0.3  # 局部选择的LS概率
RSP = 0.1  # 随机选择的RS概率
POP_SIZE = 10  # 种群规模
Max_Itertions = 100  # 最大迭代次数=100
T0_1 = 12  # 染色体长度的一半
M0 = 6  # 机器数
N = 4  # 工件数
GS_1 = int(POP_SIZE * GSP)  # 全局选择的个数
LS_1 = int(POP_SIZE * LSP)  # 局部选择的个数
RS_1 = int(POP_SIZE * RSP)  # 随机选择的个数

CSH = np.zeros([POP_SIZE, T0_1 * 2], dtype=int)  # 初始化种群
GS_MS_1 = CSH[0:GS_1, 0:T0_1]  # 机器选择部分MS
GS_OS_1 = CSH[0:GS_1, T0_1:2 * T0_1]  # 工序选择部分OS
LS_MS_1 = CSH[0:LS_1, 0:T0_1]  # 机器选择部分MS
LS_OS_1 = CSH[0:LS_1, T0_1:2 * T0_1]  # 工序选择部分OS
RS_MS_1 = CSH[0:RS_1, 0:T0_1]  # 机器选择部分MS
RS_OS_1 = CSH[0:RS_1, T0_1:2 * T0_1]  # 工序选择部分OS

O_set1 = [1, 2, 3, 4]

OS_List = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]

L = [
    [[2, 3, 4, 9999, 9999, 9999], [9999, 3, 9999, 2, 4, 9999], [1, 4, 5, 9999, 9999, 9999]],  # 第一个工件及其对应的机器加工时间
    [[3, 9999, 5, 9999, 2, 9999], [4, 3, 9999, 9999, 6, 9999], [9999, 9999, 4, 9999, 7, 11]],  # 第二个工件及其对应的机器加工时间
    [[5, 6, 9999, 9999, 9999, 9999], [9999, 4, 9999, 3, 5, 9999], [9999, 9999, 13, 9999, 9, 12]],  # 第3个，。。。。
    [[9, 9999, 7, 9, 9999, 9999], [9999, 6, 9999, 4, 9999, 5], [1, 9999, 3, 9999, 9999, 3]],  # 第4个，。。。。
]
O_L = np.array(L)


# 全局初始化
# 机器选择部分
def Global_initial(T0,O,GS,MS,n,M,OS_list,OS):
    Machine_time = np.zeros(M,dtype=float)          # 机器时间初始化
    for i in range(GS):
        random.shuffle(OS_list)  # 生成工序排序部分
        OS[i] = np.array(OS_list)
        GJ_list=[]
        for GJ_Num in range(n):         #工件集
            GJ_list.append(GJ_Num)
        random.shuffle(GJ_list)
        for g in GJ_list:    # 随机选择工件集的第一个工件,从工件集中剔除这个工件
            h = np.array(O[g])  # 第一个工件含有的工序
            for j in range(len(h)):  # 从工件的第一个工序开始选择机器
                D = np.array(h[j])
                List_Machine_weizhi = []
                for k in range(len(D)):  # 每道工序可使用的机器以及机器的加工时间
                    Useing_Machine = D[k]
                    if Useing_Machine == 9999:  # 确定可加工该工序的机器
                        continue
                    else:
                        List_Machine_weizhi.append(k)
                Machine_Select = []
                for Machine_add in List_Machine_weizhi:  # 将这道工序的可用机器时间和以前积累的机器时间相加
                    Machine_time[Machine_add] = Machine_time[Machine_add] + D[
                        Machine_add]  # 比较可用机器的时间加上以前累计的机器时间的时间值，并选出时间最小
                    Machine_Select.append(Machine_time[Machine_add])
                Min_time = min(Machine_Select)
                Machine_Index_add = Machine_Select.index(Min_time)
                MS[i][g * 3 + j] = Machine_Index_add + 1

    CHS1 = np.hstack((MS, OS))
    return CHS1


# 局部选择

def Local_initial(T0, O, LS, MS, n, M, OS_list, OS):
    for i in range(LS):
        random.shuffle(OS_list)  # 生成工序排序部分
        OS_gongxu = OS_list
        # print(OS_gongxu)
        # print('************************')
        OS[i] = np.array(OS_gongxu)
        GJ_list = []
        for GJ_Num in range(n):  # 工件集
            GJ_list.append(GJ_Num)
        A = 0
        for gon in GJ_list:
            Machine_time = np.zeros(M)  # 机器时间初始化
            g = gon  # 随机选择工件集的第一个工件   #从工件集中剔除这个工件
            h = np.array(O[g])  # 第一个工件及其对应工序的加工时间
            for j in range(len(h)):  # 从工件的第一个工序开始选择机器
                D = np.array(h[j])
                List_Machine_weizhi = []
                for k in range(len(D)):  # 每道工序可使用的机器以及机器的加工时间
                    Useing_Machine = D[k]
                    if Useing_Machine == 9999:  # 确定可加工该工序的机器
                        continue
                    else:
                        List_Machine_weizhi.append(k)
                Machine_Select = []
                for Machine_add in List_Machine_weizhi:  # 将这道工序的可用机器时间和以前积累的机器时间相加
                    Machine_time[Machine_add] = Machine_time[Machine_add] + D[
                        Machine_add]  # 比较可用机器的时间加上以前累计的机器时间的时间值，并选出时间最小
                    Machine_Select.append(Machine_time[Machine_add])
                Machine_Index_add = Machine_Select.index(min(Machine_Select))
                MS[i][g * 3 + j] = MS[i][g * 3 + j] + Machine_Index_add + 1
                A += 1
    CHS1 = np.hstack((MS, OS))
    return CHS1


# 随机选择
def Random_initial(T0, O, RS, MS, n, M, OS_list, OS):
    for i in range(RS):
        random.shuffle(OS_list)  # 生成工序排序部分
        OS_gongxu = OS_list
        OS[i] = np.array(OS_gongxu)
        GJ_list = []
        for GJ_Num in range(n):  # 工件集
            GJ_list.append(GJ_Num)
        A = 0
        for gon in GJ_list:
            Machine_time = np.zeros(M)  # 机器时间初始化
            g = gon  # 随机选择工件集的第一个工件   #从工件集中剔除这个工件
            h = np.array(O[g])  # 第一个工件及其对应工序的加工时间
            for j in range(len(h)):  # 从工件的第一个工序开始选择机器
                D = np.array(h[j])
                List_Machine_weizhi = []
                for k in range(len(D)):  # 每道工序可使用的机器以及机器的加工时间
                    Useing_Machine = D[k]
                    if Useing_Machine == 9999:  # 确定可加工该工序的机器
                        continue
                    else:
                        List_Machine_weizhi.append(k)
                Machine_Select = []
                for Machine_add in List_Machine_weizhi:  # 将这道工序的可用机器时间和以前积累的机器时间相加
                    Machine_time[Machine_add] = Machine_time[Machine_add] + D[
                        Machine_add]  # 比较可用机器的时间加上以前累计的机器时间的时间值，并选出时间最小
                    Machine_Select.append(Machine_time[Machine_add])
                Machine_Index_add = Machine_Select.index(random.choice(Machine_Select))

                MS[i][A] = MS[i][A] + Machine_Index_add + 1
                A += 1
    CHS1 = np.hstack((MS, OS))
    return CHS1

