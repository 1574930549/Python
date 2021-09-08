# -*- coding: utf-8 -*-
import 改

if __name__ == "__main__":
    # 同一个表不同文件批量改表头
    index = []
    setname = '工作表1'
    for str1 in index:
        str3 = 改.returnstr(str1)
        改.replace(str3, setname)
        print(str1,"成功")


    # 同一个文件不同表批量改表头
    # setnames=['Sheet1','Sheet2']
    # str1 = r"导出Excel2\3-27 好享购女性-6161.xlsx"
    # for setname in setnames:
    #     str3 = returnstr(str1)
    #     replace(str3, setname)
    #     print(str1,"成功")

