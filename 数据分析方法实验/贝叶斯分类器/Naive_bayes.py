import numpy as np


class Naive_bayes:
    '''
    我们需要计算先验概率，类条件密度概率，封装参数为标签和特征。
    '''
    num = 0
    feature_cat = 0
    label_cat = 0

    def __init__(self):
        pass

    def NaiveBayes(self, Py, Px_y, x):
        featrueNum = self.feature_cat
        classNum = self.label_cat
        # 建立存放所有标记的估计概率数组
        P = [0] * classNum
        # 对于每一个类别，单独估计其概率
        for i in range(classNum):
            # 初始化sum为0，sum为求和项。
            # 在训练过程中对概率进行了log处理，所以这里原先应当是连乘所有概率，最后比较哪个概率最大
            # 但是当使用log处理时，连乘变成了累加，所以使用sum
            sum = 0
            for j in range(featrueNum):
                if x[j] in Px_y[i][j]:
                    sum += Px_y[i][j][x[j]]
            P[i] = sum + Py[i]
        return P.index(max(P))

    def cost_NaiveBayes(self, Py, Px_y, x, cost):
        featrueNum = self.feature_cat
        classNum = self.label_cat
        # 建立存放所有标记的估计概率数组
        P = [0] * classNum
        P_ = [0] * classNum
        # 对于每一个类别，单独估计其概率
        for i in range(classNum):
            # 初始化sum为0，sum为求和项。
            # 在训练过程中对概率进行了log处理，所以这里原先应当是连乘所有概率，最后比较哪个概率最大
            # 但是当使用log处理时，连乘变成了累加，所以使用sum
            sum = 0
            for j in range(featrueNum):
                if x[j] in Px_y[i][j]:
                    sum += Px_y[i][j][x[j]]
            P[i] = sum + Py[i]
        for m in range(classNum):
            totall = 0
            for n in range(classNum):
                totall += P[n] * cost[m][n]
            P_[m] = totall
        return P_.index(min(P_))

    # def Naive_test(self, Py, Px_y, test_data, test_label):
    #     # 错误值计数
    #     errorCnt = 0
    #     # 循环遍历测试集中的每一个样本
    #     for i in range(len(test_data)):
    #         # 获取预测值
    #
    #         presict = self.NaiveBayes(Py, Px_y, test_data[i])
    #         # 与答案进行比较
    #         print("presict", presict)
    #         if presict != test_label[i]:
    #             # 若错误  错误值计数加1
    #             errorCnt += 1
    #     # 返回准确率
    #     return 1 - (errorCnt / len(test_data))

    def Naive_test(self, Py, Px_y, test_data, test_label):
        # 错误值计数
        n1 = 0
        n2 = 0
        n3 = 0
        n0 = 0
        # 循环遍历测试集中的每一个样本
        for i in range(len(test_data)):
            # 获取预测值
            presict = self.NaiveBayes(Py, Px_y, test_data[i])
            # 与答案进行比较

            if test_label[i] == 0:
                n0 += 1
            elif test_label[i] == 1:
                n1 += 1
            elif test_label[i] == 2:
                n2 += 1
            elif test_label[i] == 3:
                n3 += 1

        # 返回准确率
        return n0 / len(test_data), n1 / len(test_data), n2 / len(test_data), n3 / len(test_data)

    def cost_Naive_test(self, Py, Px_y, test_data, test_label, cost):
        # 错误值计数
        errorCnt = 0
        # 循环遍历测试集中的每一个样本
        for i in range(len(test_data)):
            # 获取预测值
            presict = self.cost_NaiveBayes(Py, Px_y, test_data[i], cost)
            # 与答案进行比较

            if presict != test_label[i]:
                # 若错误  错误值计数加1
                errorCnt += 1
        # 返回准确率
        return 1 - (errorCnt / len(test_data))

    def fit(self, train_data, train_label):
        featureNum = train_data.shape[1]
        self.feature_cat = featureNum
        label = set(train_label)
        self.label_cat = len(label)
        classNum = len(label)
        Py = np.zeros((classNum, 1))
        # 计算先验概率分布
        label_dic = {}
        for i in label:
            # 若训练集中没有某一类的数据则其预测概率为零。加一保证不为零，还要同时保证分母不为零 确保预测概率不为零
            label_dic[i] = ((np.sum(train_label == i)) + 1)
            Py[int(i)] = (label_dic[i]) / (len(train_label) + classNum)
        # 转换为log对数形式，防止数据下溢
        Py = np.log(Py)
        # 初始化为全0矩阵，用于存放所有情况下的条件概率
        Px_y = {}
        for i in range(classNum):
            Px_y[i] = {}
            for j in range(featureNum):
                Px_y[i][j] = {}
        for m in range(len(train_label)):
            label = train_label[m]
            x = train_data[m]
            for n in range(featureNum):
                # 这里还没有计算条件概率，先把所有数累加，全加完以后，在后续步骤中再求对应的条件概率
                if x[n] not in Px_y[label][n]:
                    Px_y[label][n][x[n]] = 1
                else:
                    Px_y[label][n][x[n]] += 1
        for label in range(classNum):
            for z in range(featureNum):
                l = len(Px_y[label][z].keys())
                for key, item in Px_y[label][z].items():
                    Px_y[label][z][key] = np.log((item + 1) / (label_dic[label]) + l)
        # 返回先验概率分布和条件概率分布
        return Py, Px_y
