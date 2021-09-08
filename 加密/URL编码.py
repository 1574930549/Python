# -*- coding:UTF-8 -*-
__author__ = 'rxz'

from urllib import parse

a = parse.quote("中国欢迎您")
print(a)  # %E4%B8%AD%E5%9B%BD%E6%AC%A2%E8%BF%8E%E6%82%A8

b = parse.unquote(a)
print(b)  # 中国欢迎您