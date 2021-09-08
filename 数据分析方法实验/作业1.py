from sklearn import datasets
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import copy


def find_neighbor(j, x, eps):
    N = list()
    for i in range(x.shape[0]):
        temp = np.sqrt(np.sum(np.square(x[j] - x[i])))  # 计算欧式距离
        if temp <= eps:
            N.append(i)
    return set(N)


def DBSCAN(X, eps, min_Pts):
    k = -1
    neighbor_list = []  # 用来保存每个数据的邻域
    omega_list = []  # 核心对象集合
    gama = set([x for x in range(len(X))])  # 初始时将所有点标记为未访问
    cluster = [-1 for _ in range(len(X))]  # 聚类
    marker = ["s" for _ in range(len(X))]
    for i in range(len(X)):
        neighbor_list.append(find_neighbor(i, X, eps))
        if len(neighbor_list[-1]) >= min_Pts:
            omega_list.append(i)  # 将样本加入核心对象集合
    omega_list = set(omega_list)  # 转化为集合便于操作
    while len(omega_list) > 0:
        gama_old = copy.deepcopy(gama)
        j = random.choice(list(omega_list))  # 随机选取一个核心对象
        k = k + 1
        Q = list()
        Q.append(j)
        gama.remove(j)
        while len(Q) > 0:
            q = Q[0]
            Q.remove(q)
            if len(neighbor_list[q]) >= min_Pts:
                delta = neighbor_list[q] & gama
                deltalist = list(delta)
                for i in range(len(delta)):
                    Q.append(deltalist[i])
                    gama = gama - delta
        Ck = gama_old - gama
        Cklist = list(Ck)
        for i in range(len(Ck)):
            cluster[Cklist[i]] = k
            marker[Cklist[i]] = "o"
        omega_list = omega_list - Ck
    return cluster, marker


if __name__ == "__main__":
    centers = [[5, 5], [7, 6], [7, 3]]
    # 产生的数据个数
    n_samples = 500
    # 生产数据:此实验结果受cluster_std的影响，或者说受eps 和cluster_std差值影响
    X, lables_true = datasets.make_blobs(n_samples=n_samples, centers=centers, cluster_std=0.4,
                                         random_state=0, center_box=(0, 10))
    # n_samples(int/array):如果参数为int，代表总样本数；如果参数为array-like，数组中的每个数代表每一簇的样本数。
    # n_features(int):样本点的维度。
    # centers(int):样本中心数。如果样本数为int且centers=None，生成三个样本中心；如果样本数（n_samples）为数组，则centers 要么为None，要么为数组的长度。
    # cluster_std(float/sequence of floats):样本中，簇的标准差。
    # center_box(pair of floats (min, max)):每个簇的上下限。
    # shuffle(boolean):是否将样本打乱。
    # random_state(int/RandomState instance /None):指定随机数种子，每个种子生成的序列相同，与minecraft地图种子同理。

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()
    X = np.array(X)
    eps = 0.3
    min_Pts = 10
    begin = time.time()
    C, k = DBSCAN(X, eps, min_Pts)
    end = time.time()
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=C)
    plt.show()
