# -*- coding: utf-8 -*-
import 录
import time


if __name__ == "__main__":
    start = time.time()
    # 同一个文件不同表批量录入
    # setnames=['Sheet1','已达']
    # str1 = r""
    # for setname in setnames:

    # 同一个表不同文件批量录入
    index = []
    setname = 'Sheet1'  # Sheet1 工作表1
    for str1 in index:

        str1 = str1.replace("D:\\XZ\\", "")
        str3 = './' + str1

        # 改过表头的要加上xls文件末尾要加上x
        # if str1.find("xlsx") != -1:
        #     str1 = str1
        # elif str1.find("XLSx") != -1:
        #     str1 = str1
        # else:
        #     str1 = str1 + "x"

        engine = 录.query()
        str2 = 录.returnstr(str1)

        录.insql(str2, engine, setname)

        sql = 'SELECT count(1) FROM `t_kdxx_all_2`;'
        n = 录.queryGp(sql, engine)

        录.write(str3, n)
        print(str1, "成功")
    end = time.time()
    print("执行时间", end - start)
