# -*- coding:UTF-8 -*-
__author__ = 'rxz'

import binascii

# 方法中不传参数则是以默认的utf-8编码进行转换
a = "中国欢迎您".encode("utf-8")
print(a)  # b'\xe4\xb8\xad\xe5\x9b\xbd\xe6\xac\xa2\xe8\xbf\x8e\xe6\x82\xa8'

c = binascii.b2a_hex('中国欢迎您'.encode())
print("c===", c)  # c=== b'e4b8ade59bbde6aca2e8bf8ee682a8'

d = binascii.a2b_hex(c)
print(d)  # b'\xe4\xb8\xad\xe5\x9b\xbd\xe6\xac\xa2\xe8\xbf\x8e\xe6\x82\xa8'

v = binascii.a2b_hex(c).decode("utf-8")
print(v)  # 中国欢迎您
b = a.decode("utf-8")
print(b)  # 中国欢迎您