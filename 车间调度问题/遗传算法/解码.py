import numpy as np
import random

T0_1 = 12  # 染色体长度的一半
N = 4  # 工件数
L = [
    [[2, 3, 4, 9999, 9999, 9999], [9999, 3, 9999, 2, 4, 9999], [1, 4, 5, 9999, 9999, 9999]],  # 第一个工件及其对应的机器加工时间
    [[3, 9999, 5, 9999, 2, 9999], [4, 3, 9999, 9999, 6, 9999], [9999, 9999, 4, 9999, 7, 11]],  # 第二个工件及其对应的机器加工时间
    [[5, 6, 9999, 9999, 9999, 9999], [9999, 4, 9999, 3, 5, 9999], [9999, 9999, 13, 9999, 9, 12]],  # 第3个，。。。。
    [[9, 9999, 7, 9, 9999, 9999], [9999, 6, 9999, 4, 9999, 5], [1, 9999, 3, 9999, 9999, 3]],  # 第4个，。。。。
]
O_L = np.array(L)

CHS_0 = [3, 1, 1, 2, 1, 2, 1, 1, 3, 1, 3, 1, 4, 1, 3, 1, 2, 2, 4, 3, 1, 4, 3, 2]


def Chromosome_decoding(CHS, O, T0, n):
    # print(CHS_0)
    JM = np.zeros((4, 3), dtype=int)  # JM(j,h)表示工件Ji的工序Oh的机器号
    T = np.zeros((4, 3), dtype=int)  # T（j,h）表示工件Jj的工序Oh的加工时间

    # 步骤1：对机器选择部分进行解码，从左到右依次读取并转换成机器顺序矩阵JM和时间顺序矩阵T
    # MS = []
    # OS = []
    MS = CHS[0:12]
    OS = CHS[12:24]
    # 将CHS初始化矩阵转化为MS、OS两个矩阵
    # for i in range(2 * T0):
    #     if i < T0:
    #         MS.append(CHS[i])
    #     else:
    #         OS.append(CHS[i])
    GX_num = 0
    for J_j in MS:  # 将机器选择部分转换成机器顺序矩阵和时间顺序矩阵
        GX_num += 1
        JM_j = int((GX_num - 1) / 3)  # 机器顺序矩阵的横坐标
        JM_h = int((GX_num - 1) % 3)  # 机器顺序矩阵的纵坐标
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
    print(JM, T)

    # 步骤2：按照步骤1对应的T和JM依次得到每个工件工序对应的加工机器和加工时间
    Start_time = np.zeros((6, 12), dtype=int)  # 机器开始加工的时间
    End_time = np.zeros((6, 12), dtype=int)  # 机器结束加工的时间
    Opearation = np.zeros((6, 12), dtype=int)

    Counter_List = []
    T_count = 0
    for OS_j in OS:  # 通过机器顺序矩阵和时间顺序矩阵的到工序的加工机器和加工时间
        # print(OS_j)
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
            # print(OS_j)
            Start_time[M_i][T_count - 1] = 0
            # print(OS_j)
            End_time[M_i][T_count - 1] += P_ij
            Opearation[M_i][T_count - 1] = OS_j
            # print(End_time)
        # 工序O_jh是机器M_i的第一道工序
        elif len(M_n_list) == 0 and M_i_h > 1:
            # print(OS_j,M_i_h,'#')
            # 寻找该工件上一道工序的完工时间：
            SD_Machine = JM[OS_j - 1][M_i_h - 2]
            SD_count = 0
            SD_c = 0
            for SD_i in OS:
                SD_count += 1
                if SD_i == OS_j:
                    # print(SD_i,'%')
                    SD_c += 1
                    if SD_c == M_i_h - 1:
                        # print('#')
                        break
            # print(SD_count,SD_Machine)

            S = End_time[SD_Machine][SD_count - 1]
            # print(S)
            Start_time[M_i][T_count - 1] = S
            End_time[M_i][T_count - 1] = S + P_ij
            Opearation[M_i][T_count - 1] = OS_j

        elif len(M_n_list) != 0 and M_i_h == 1:
            # print(OS_j,M_i_h,'##')
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
            # print(A,B)
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
            # print(End_time)

        # 加工工序不是机器和工件的第一道工序
        else:
            print(OS_j, M_i_h, '*')
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
                    Lst_index_1.append(Lst_index_1[L_j_1])
            if len(Lst_1) != 0:
                L_M_1_list = []
                for L_M_1 in Lst_1:
                    L_M_1_list.append(L_M_1)
                    if L_M_1 >= P_ij:
                        List_Count_1 = List_index_1[Lst_index_1.index(L_M_1)]
                        L_M = List_index_1[Lst_1.index(L_M_1)]
                        break
                    if End_time[M_i][List_Count_1] >= SC_endtime or Start_time[M_i][L_M] - SC_endtime >= 0:
                        Start_time[M_i][T_count - 1] = End_time[M_i][List_Count_1]
                        break
                    while len(L_M_1_list) == len(Lst_1):
                        Start_time[M_i][T_count - 1] = max(End_time[M_i])
                        break
            else:
                Start_time[M_i][T_count - 1] = max(End_time[M_i])
            End_time[M_i][T_count - 1] = Start_time[M_i][T_count - 1] + P_ij
            Opearation[M_i][T_count - 1] = OS_j
            print(End_time)
    return Start_time, End_time, Opearation


print(Chromosome_decoding(CHS_0, O_L, T0_1, N))
