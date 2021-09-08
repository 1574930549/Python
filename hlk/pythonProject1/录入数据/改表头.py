# -*- coding: utf-8 -*-
import 改

if __name__ == "__main__":



    # str1 = "test\\test.xls"
    str1 = r""
    str1 = str1.replace("D:\\XZ\\", "")
    # setname='工作表1'# Sheet1 工作表1
    setname = 'Sheet1'
    # setname = '6'  # Sheet1 工作表1
    # setname = '酒'  # Sheet1 工作表1
    # setname = '蜂胶'  # Sheet1 工作表1
    # setname = '白酒'  # Sheet1 工作表1

    str3 = 改.returnstr(str1)
    改.replace(str3, setname)
