# -*- coding: utf-8 -*-
import 录
import time
if __name__ == "__main__":
    start = time.time()
    engine = 录.query()
    # setname='工作表1'# Sheet1 工作表1
    setname = 'Sheet1'  # Sheet1 工作表1
    # setname = '乐拍'  # Sheet1 工作表1
    # setname = '白酒'  # Sheet1 工作表1
    # setname = '酒'  # Sheet1 工作表1
    # setname = '蜂胶'  # Sheet1 工作表1
    str1 = r""
    #
    # #
    str1=str1.replace("D:\\XZ\\","")
    str3 = './' + str1
    # str1=str1+"x"#改过表头的要加上xls文件末尾要加上x
    str2 = 录.returnstr(str1)

    录.insql(str2, engine, setname)

    sql = 'SELECT count(1) FROM `t_kdxx_all_2`;'
    n= 录.queryGp(sql, engine)

    录.write(str3, n)
    print(str3,setname)
    end = time.time()
    print("执行时间", end - start)
