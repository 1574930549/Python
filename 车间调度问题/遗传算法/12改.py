import numpy as np
import matplotlib.pyplot as plt
import random
import itertools


# 全局初始化
def Global_initial(T0, O, GS, MS, n, M, OS_list, OS):
    Machine_time = np.zeros(M, dtype=int)  # 机器时间初始化
    for i in range(GS):
        random.shuffle(OS_list)  # 生成工序排序部分
        OS[i] = np.array(OS_list)
        GJ_list = []
        for GJ_Num in range(n):  # 工件集
            GJ_list.append(GJ_Num)
        random.shuffle(GJ_list)
        for g in GJ_list:  # 随机选择工件集的第一个工件,从工件集中剔除这个工件
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


# 染色体解码
# JM与T的关系是一一对应的
def Chromosome_decoding(CHS, O, T0, n, Max_Onum, M0):
    JM = np.zeros((n, Max_Onum), dtype=int)  # JM(j,h)表示工件Ji的工序Oh的机器号
    T = np.zeros((n, Max_Onum), dtype=int)  # T（j,h）表示工件Jj的工序Oh的加工时间

    # 步骤1：对机器选择部分进行解码，从左到右依次读取并转换成机器顺序矩阵JM和时间顺序矩阵T
    MS = CHS[0:T0]
    OS = CHS[T0:T0*2]
    GX_num = 0
    for J_j in MS:  # 将机器选择部分转换成机器顺序矩阵和时间顺序矩阵
        GX_num += 1
        JM_j = int((GX_num - 1) / Max_Onum)  # 机器顺序矩阵的横坐标
        JM_h = int((GX_num - 1) % Max_Onum)  # 机器顺序矩阵的纵坐标
        O_j = np.array(O[JM_j][JM_h])
        Mac_using = []
        Mac_time = []
        for Mac_num in range(len(O_j)):  # 寻找MS对应部分的机器时间和机器顺序
            if O_j[Mac_num] != 9999:
                Mac_using.append(Mac_num)
                Mac_time.append(O_j[Mac_num])
            else:
                continue
        JM[JM_j][JM_h] += Mac_using[J_j - 1]  # 机器顺序矩阵
        T[JM_j][JM_h] += Mac_time[J_j - 1]  # 时间顺序矩阵

    # 步骤2：按照步骤1对应的T和JM依次得到每个工件工序对应的加工机器和加工时间
    Start_time = np.zeros((M0, T0), dtype=int)  # 机器开始加工的时间
    End_time = np.zeros((M0, T0), dtype=int)  # 机器结束加工的时间
    Opearation = np.zeros((M0, T0), dtype=int)

    Counter_List = []
    T_count = 0
    for OS_j in OS:  # 通过机器顺序矩阵和时间顺序矩阵的到工序的加工机器和加工时间
        T_count += 1
        Counter_List.append(OS_j)
        M_i_h = Counter_List.count(OS_j)  # 该工件的第几道工序
        M_i = JM[OS_j - 1][M_i_h - 1]  # 这道工序使用的机器
        P_ij = T[OS_j - 1][M_i_h - 1]  # 这道工序的加工时间
        M_n_list = []
        for M_n in End_time[M_i]:  # 确定工序为机器M_i的第几道加工工序
            if M_n != 0:
                M_n_list.append(M_n)
        # 工件O_jh是机器M_i的第一道加工工序，直接从机器M_i的零时刻进行加工
        if M_i_h == 1 and len(M_n_list) == 0:
            Start_time[M_i][T_count - 1] = 0
            End_time[M_i][T_count - 1] += P_ij
            Opearation[M_i][T_count - 1] = OS_j
        # 工序O_jh是机器M_i的第一道工序
        elif len(M_n_list) == 0 and M_i_h > 1:
            # 寻找该工件上一道工序的完工时间：
            SD_Machine = JM[OS_j - 1][M_i_h - 2]
            SD_count = 0
            SD_c = 0
            for SD_i in OS:
                SD_count += 1
                if SD_i == OS_j:
                    SD_c += 1
                    if SD_c == M_i_h - 1:
                        break

            S = End_time[SD_Machine][SD_count - 1]
            Start_time[M_i][T_count - 1] = S
            End_time[M_i][T_count - 1] = S + P_ij
            Opearation[M_i][T_count - 1] = OS_j

        elif len(M_n_list) != 0 and M_i_h == 1:
            List_start_0 = []
            List_end_0 = []
            List_index_0 = []
            for L_i in range(len(End_time[M_i])):
                if End_time[M_i][L_i] != 0:
                    List_start_0.append(Start_time[M_i][L_i])
                    List_end_0.append(End_time[M_i][L_i])
                    List_index_0.append(L_i)
            disp = zip(List_index_0, List_end_0)
            disp_1 = zip(List_index_0, List_start_0)
            Disp_1 = dict(disp)
            Disp_2 = dict(disp_1)
            A = sorted(Disp_1.items(), key=lambda item: item[1])
            B = sorted(Disp_2.items(), key=lambda item: item[1])
            D_1 = dict(A)
            D_2 = dict(B)
            List_start = []
            List_end = []
            List_index = []
            for k in D_1:
                List_end.append(D_1[k])
                List_index.append(k)
            for k_1 in D_2:
                List_start.append(D_2[k_1])
            Lst = []
            Lst_index = []
            for L_j in range(len(List_end) - 1):
                if List_start[L_j + 1] - List_end[L_j] >= P_ij:
                    Lst.append(List_start[L_j + 1] - List_end[L_j])
                    Lst_index.append(List_index[L_j])
            if len(Lst) != 0:
                L_m_list = []
                for L_m in Lst:
                    L_m_list.append(L_m)
                    if L_m >= P_ij:
                        L_P = Lst_index[Lst.index(L_m)]
                        Start_time[M_i][T_count - 1] = End_time[M_i][L_P]
                        break
                    while len(L_m_list) == len(Lst):
                        Start_time[M_i][T_count - 1] = max(End_time[M_i])
                        break
            else:
                Start_time[M_i][T_count - 1] = max(End_time[M_i])
            End_time[M_i][T_count - 1] = Start_time[M_i][T_count - 1] + P_ij
            Opearation[M_i][T_count - 1] = OS_j

        # 加工工序不是机器和工件的第一道工序
        else:
            SC_Machine = JM[OS_j - 1][M_i_h - 2]  # 这个工件上一道工序的使用机器
            CO_er = 0
            CON_er = 0
            for Max_i in OS:
                CO_er += 1
                if Max_i == OS_j:
                    CON_er += 1
                    if CON_er == M_i_h - 1:
                        break
            SC_endtime = End_time[SC_Machine][CO_er - 1]  # 这个工件的上一道工序的结束时间
            SD_S = []
            SD_E = []
            SD_index = []
            for SD_i in range(len(End_time[M_i])):
                if End_time[M_i][SD_i] != 0:
                    SD_E.append(End_time[M_i][SD_i])
                    SD_S.append(Start_time[M_i][SD_i])
                    SD_index.append(SD_i)
            disp_2 = zip(SD_index, SD_E)
            disp_3 = zip(SD_index, SD_S)
            Disp_3 = dict(disp_2)
            Disp_4 = dict(disp_3)
            C_1 = sorted(Disp_3.items(), key=lambda item: item[1])
            D_4 = sorted(Disp_4.items(), key=lambda item: item[1])
            D_5 = dict(C_1)
            D_6 = dict(D_4)
            List_start_1 = []
            List_end_1 = []
            List_index_1 = []
            for k_2 in D_5:
                List_end_1.append(D_5[k_2])
                List_index_1.append(k_2)
            for k_3 in D_6:
                List_start_1.append(D_6[k_3])
            Lst_1 = []
            Lst_index_1 = []
            for L_j_1 in range(len(List_end_1) - 1):
                if List_start_1[L_j_1 + 1] - List_end_1[L_j_1] >= P_ij:
                    Lst_1.append(List_start_1[L_j_1 + 1] - List_end_1[L_j_1])
                    Lst_index_1.append(List_index_1[L_j_1])
            if len(Lst_1) != 0:
                L_M_1_list = []
                for L_M_1 in Lst_1:
                    L_M_1_list.append(L_M_1)
                    if L_M_1 >= P_ij:
                        List_Count_1 = Lst_index_1[Lst_1.index(L_M_1)]
                        L_M = List_index_1[List_index_1.index(List_Count_1) + 1]
                        if End_time[M_i][List_Count_1] >= SC_endtime or Start_time[M_i][L_M] - SC_endtime >= P_ij:
                            Start_time[M_i][T_count - 1] = End_time[M_i][List_Count_1]
                            break
                    while len(L_M_1_list) == len(Lst_1):
                        if max(End_time[M_i]) >= SC_endtime:
                            Start_time[M_i][T_count - 1] = max(End_time[M_i])
                        else:
                            Start_time[M_i][T_count - 1] = SC_endtime
                        break

            else:
                if max(End_time[M_i]) >= SC_endtime:
                    Start_time[M_i][T_count - 1] = max(End_time[M_i])
                else:
                    Start_time[M_i][T_count - 1] = SC_endtime
            End_time[M_i][T_count - 1] = Start_time[M_i][T_count - 1] + P_ij
            Opearation[M_i][T_count - 1] = OS_j
    return Start_time, End_time, Opearation


# 交叉操作
# 机器选择部分
def Crossover_Machine(T0, T_r, CHS1, CHS2):
    r = random.randint(0, T0)  # 在区间[遗传算法,T0]内产生一个整数r
    random.shuffle(T_r)
    R = T_r[0:r]  # 按照随机数r产生r个互不相等的整数
    # 将父代的染色体复制到子代中去，保持他们的顺序和位置
    C_1 = CHS2
    C_2 = CHS1
    for i in R:
        K = CHS1[i]
        K_2 = CHS2[i]
        C_1[i] = K
        C_2[i] = K_2
    return C_1, C_2


# 工序排序部分
def Crossover_Operation(O_set, CHS1, CHS2, T0, N):
    r = random.randint(1, T0)
    random.shuffle(O_set)
    O_1 = O_set[0:r]  # 将工件集划分为Jobset1和Jobset2
    O_2 = O_set[r:N]
    C_1 = np.zeros(T0, dtype=int)
    C_2 = np.zeros(T0, dtype=int)
    Count_i = 0
    Count = 0
    C_index1 = []
    C_index2 = []
    for j in CHS1:  # 复制父代染色体P1、P2中包含工件集Jobset1/Jobset2中的工件复制到C1/C2中，保持他们的顺序
        Count_i += 1
        for i in O_1:
            if j == i:
                C_1[Count_i - 1] = j
    for j_1 in CHS2:
        Count += 1
        for i_1 in O_2:
            if j_1 == i_1:
                C_2[Count - 1] = j_1
    Count_2 = 0
    for j_2 in CHS1:
        Count_2 += 1
        for i_2 in O_2:
            if j_2 == i_2:
                C_index1.append(Count_2 - 1)
    Count_3 = 0
    for j_3 in CHS2:
        Count_3 += 1
        for i_3 in O_1:
            if j_3 == i_3:
                C_index2.append(Count_3 - 1)
    new_CHS1 = np.delete(CHS1, C_index1)
    new_CHS2 = np.delete(CHS2, C_index2)
    Count_4 = 0
    for k in range(len(CHS1)):
        if C_1[k] == 0:
            C_1[k] = new_CHS2[Count_4]
            Count_4 += 1
    Count_5 = 0
    for k_1 in range(len(CHS2)):
        if C_2[k_1] == 0:
            C_2[k_1] = new_CHS1[Count_5]
            Count_5 += 1
    return C_1, C_2


# 变异操作
# 机器变异部分
def Variation_Machine(Tr, O, MS, T0, Max_Onum):
    # 机器选择部分
    r = random.randint(1, T0 - 1)  # 在变异染色体中选择r个位置
    random.shuffle(Tr)
    T_r = Tr[0:r]
    for i in T_r:
        O_i = int(i / Max_Onum)
        O_j = i % Max_Onum
        Machine_using = O[O_i][O_j]
        Machine_index = []
        for j in Machine_using:
            if j != 9999:
                Machine_index.append(j)
        Min = Machine_index[0]
        Min_index = 0
        for j_1 in range(len(Machine_index)):
            if Machine_index[j_1] < Min:
                Min = Machine_index[j_1]
                Min_index = j_1
            else:
                Min = Min
                Min_index = Min_index
        MS[i] = Min_index + 1
    return MS


# 变异操作
# 工序变异部分
def Variation_Operation(Tr, OS, MS):
    r = random.randint(2, 6)  # 在变异染色体中选择r个位置
    random.shuffle(Tr)
    T_r = Tr[0:r]
    O_ky = []
    for i in range(len(OS)):
        for j in range(len(T_r)):
            if i == T_r[j]:
                O_ky.append(OS[i])
    # print(O_ky)
    A = np.array(list(itertools.permutations(O_ky, r)))
    CHS_T = []
    for k in range(len(A)):
        H = A[k]
        for k_1 in range(len(T_r)):
            I_1 = T_r[k_1]
            I_2 = H[k_1]
            OS[I_1] = I_2
        CHS = MS + OS
        CHS_T.append(list(CHS))
    M = np.array(CHS_T)
    W = fitness(M, k + 1)
    Fit_index = []
    for i_1 in range(k + 1):
        Fit_index.append(i_1)
    disp = zip(Fit_index, W)
    Disp = dict(disp)
    B_1 = sorted(Disp.items(), key=lambda item: item[1])
    B = dict(B_1)
    B_0 = list(B.keys())
    B0 = B_0[0]
    return CHS_T[B0]


# 选择操作
def Select(Fit_value, POP_SIZE):
    Fit_index = []
    for i in range(POP_SIZE):
        Fit_index.append(i)
    # print(Fit_index,Fit_value)
    disp = zip(Fit_index, Fit_value)
    Disp = dict(disp)
    A = sorted(Disp.items(), key=lambda item: item[1])
    D = dict(A)
    Pop_leave = int(POP_SIZE * 0.6)
    CHS_index = []
    for j, (k, v) in enumerate(D.items()):
        if j in range(0, Pop_leave):
            CHS_index.append(k)
    return CHS_index


# 画甘特图
def gatt(End_time, Start_time, CHS):
    Start = []
    End = []
    M = ['red', 'blue', 'yellow', 'orange', 'green']
    for i in range(6):
        for j in range(12):
            if End_time[i][j] != 0:
                plt.barh(i, width=End_time[i][j] - Start_time[i][j], left=Start_time[i][j], color=M[CHS[j + 12] - 1],
                         edgecolor='white')
                plt.text(x=Start_time[i][j] + 0.3, y=i, s=(CHS[j + 12], End_time[i, j]))
                Start.append(Start_time[i][j])
                End.append(End_time[i][j])
    plt.yticks(np.arange(i + 1), np.arange(1, i + 2))
    plt.show()


def main():
    GSP = 0.6  # 全局选择的GS概率
    LSP = 0.3  # 局部选择的LS概率
    RSP = 0.1  # 随机选择的RS概率
    POP_SIZE = 100  # 种群规模
    Max_Itertions = 100  # 最大迭代次数=100
    T0_1 = 12  # 染色体长度的一半
    M0 = 6  # 机器数4
    N = 4  # 工件数3
    Max_Onum = 3  # 所有工件中，最大的工序数
    GS_1 = int(POP_SIZE * GSP)  # 全局选择的个数
    LS_1 = int(POP_SIZE * LSP)  # 局部选择的个数
    RS_1 = int(POP_SIZE * RSP)  # 随机选择的个数
    T_R = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    CSH = np.zeros([POP_SIZE, T0_1 * 2], dtype=int)  # 初始化种群
    GS_MS_1 = np.zeros([GS_1, T0_1], dtype=int)  # 机器选择部分MS
    GS_OS_1 = np.zeros([GS_1, T0_1], dtype=int)  # 工序选择部分OS
    LS_MS_1 = np.zeros([LS_1, T0_1], dtype=int)  # 机器选择部分MS
    LS_OS_1 = np.zeros([LS_1, T0_1], dtype=int)  # 工序选择部分OS
    RS_MS_1 = np.zeros([RS_1, T0_1], dtype=int)  # 机器选择部分MS
    RS_OS_1 = np.zeros([RS_1, T0_1], dtype=int)  # 工序选择部分OS

    O_set1 = [1, 2, 3, 4]

    OS_List = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]

    L = [
        [[2, 3, 4, 9999, 9999, 9999], [9999, 3, 9999, 2, 4, 9999], [1, 4, 5, 9999, 9999, 9999]],  # 第一个工件及其对应的机器加工时间
        [[3, 9999, 5, 9999, 2, 9999], [4, 3, 9999, 9999, 6, 9999], [9999, 9999, 4, 9999, 7, 11]],  # 第二个工件及其对应的机器加工时间
        [[5, 6, 9999, 9999, 9999, 9999], [9999, 4, 9999, 3, 5, 9999], [9999, 9999, 13, 9999, 9, 12]],  # 第3个，。。。。
        [[9, 9999, 7, 9, 9999, 9999], [9999, 6, 9999, 4, 9999, 5], [1, 9999, 3, 9999, 9999, 3]],  # 第4个，。。。。
    ]
    O_L = np.array(L)
    CHS0 = Global_initial(T0_1, O_L, GS_1, GS_MS_1, N, M0, OS_List, GS_OS_1)  # 全局选择部分染色体
    CHS1 = Local_initial(T0_1, O_L, LS_1, LS_MS_1, N, M0, OS_List, LS_OS_1)  # 局部训责部分染色体
    CHS2 = Random_initial(T0_1, O_L, RS_1, RS_MS_1, N, M0, OS_List, RS_OS_1)  # 随机选择部分染色体
    C = np.vstack((CHS0, CHS1, CHS2))  # 将初始化染色体合并到一个矩阵
    Fit = []
    for i in range(len(C)):  # 计算每个染色体个体的适应度
        M = C[i]
        A = Chromosome_decoding(M, O_L, T0_1, N, Max_Onum, M0)
        F = np.max(A[1])
        Fit.append(F)
    Min = min(Fit)
    while Max_Itertions > 0:  # 设定结束的约束条件
        Max_Itertions -= 1
        S = Select(Fit, POP_SIZE)
        C_I = []
        for j in S:
            C_I.append(C[j])
        C_J = np.array(C_I)
        P_c = random.uniform(0.6, 0.8)  # 确定交叉概率
        P_m = random.uniform(0.005, 0.006)  # 确定变异概率
        P_C = int(P_c * (len(S)))
        P_M = int(P_m * (len(S)))
        S_list = np.random.permutation(range(len(S)))
        PC = S_list[0:P_C]
        for k in range(0, len(PC), 2):
            CHS_1 = C_J[PC[k]]
            if k + 1 < len(PC):
                CHS_2 = C_J[PC[k + 1]]
            else:
                break
            MS_crossover = Crossover_Machine(T0_1, T_R, CHS_1[0:T0_1], CHS_2[0:T0_1])
            OS_crossover = Crossover_Operation(O_set1, CHS_1[T0_1:T0_1*2], CHS_2[T0_1:T0_1*2], T0_1, N)
            CHS_crossover_1 = np.hstack((MS_crossover[0], OS_crossover[0]))
            CHS_crossover_2 = np.hstack((MS_crossover[1], OS_crossover[1]))
            CHS_crossover = np.vstack((CHS_crossover_1, CHS_crossover_2))
            C_J = np.vstack((C_J, CHS_crossover))
        Fit_1 = []
        for i_1 in range(len(C_J)):  # 计算每个染色体个体的适应度
            M_0 = C_J[i_1]
            A = Chromosome_decoding(M_0, O_L, T0_1, N, Max_Onum, M0)
            F = np.max(A[1])
            Fit_1.append(F)
        Min_1 = min(Fit_1)

        if Min_1 < Min:
            Min = Min_1
            S_1 = Select(Fit_1, len(C_J))
            Min_Index = S_1[0]
            Min_CHS = C_J[Min_Index]
    Chromo = Chromosome_decoding(Min_CHS, O_L, T0_1, N, Max_Onum, M0)
    print('最优解为：',Min)
    gatt(Chromo[1], Chromo[0], Min_CHS)  # 画甘特图


main()
