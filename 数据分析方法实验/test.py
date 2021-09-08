import pandas as pd
import numpy as np


def readexcel(fileName):
    fileName=r"C:\Users\zlh\Desktop\数据分析方法实验\实验三、四\play.xlsx"
    data = pd.read_excel(fileName)
    # print(type(data))
    train_data = np.array(data)  # np.ndarray()
    excel_list = train_data.tolist()  # list
    print(excel_list)

    return excel_list

if __name__=="__main__":
    fileName=r"C:\Users\zlh\Desktop\数据分析方法实验\实验三、四\play.xlsx"
    readexcel(fileName)

