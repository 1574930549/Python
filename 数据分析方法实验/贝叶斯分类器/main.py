import Naive_bayes

from sklearn.model_selection import RepeatedKFold
from sklearn import preprocessing
import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.read_excel(r"C:\Users\zlh\Desktop\数据分析方法实验\实验三、四\test.xlsx")
    raw_set = df.values
    label_encoder = []
    #  放置每一列的encoder
    encoded_set = np.empty(raw_set.shape)
    for i, _ in enumerate(raw_set[0]):
        # 拟合每一列上的数据
        encoder = preprocessing.LabelEncoder()
        encoded_set[:, i] = encoder.fit_transform(raw_set[:, i])
        label_encoder.append(encoder)
    dataset_X = encoded_set[:, :-1].astype(int)
    dataset_y = encoded_set[:, -1].astype(int)
    #  将数据集拆分为train set 和test set      start = time.time()
    naive_bys = Naive_bayes.Naive_bayes()
    # 使用习得的先验概率分布和条件概率分布对测试集进行测试
    kf = RepeatedKFold(n_splits=10)
    n0 = 0
    n1 = 0
    n2 = 0
    n3 = 0
    Accuracy0 = 0
    Accuracy1 = 0
    Accuracy2 = 0
    Accuracy3 = 0
    for train_index, test_index in kf.split(dataset_X):
        train_X, train_y = dataset_X[train_index], dataset_y[train_index]
        test_X, test_y = dataset_X[test_index], dataset_y[test_index]
        Py, Px_y = naive_bys.fit(train_X, train_y)
        n0, n1, n2, n3 = naive_bys.Naive_test(Py, Px_y, test_X, test_y)
        Accuracy0 += n0
        Accuracy1 += n1
        Accuracy2 += n2
        Accuracy3 += n3
        # print(naive_bys.Naive_test(Py, Px_y, test_X, test_y))
    print("class  \t  N\t\t\tN[%]")
    print('acc:   \t', np.sum(dataset_y == 0), '  \t%f' % Accuracy0, "%")
    print('good:  \t', np.sum(dataset_y == 1), '   \t%f' % Accuracy1, "%")
    print('unacc: \t', np.sum(dataset_y == 2), ' \t%f' % Accuracy2, "%")
    print('v-good:\t', np.sum(dataset_y == 3), '   \t%f' % Accuracy3, "%")
    print("这里Word里面有个错误，总数据行数为1576，而1210+384+69+65=",1210+384+69+65)
    print("所以N[%]也不一定是对的，而我的N[%]相加为",Accuracy0 + Accuracy1 + Accuracy2 + Accuracy3)
    print("近似100%（由于int转flot或flot转int时取舍导致的误差）")

