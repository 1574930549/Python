#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def removeKdigits(num, k):
    num1 = list(num)
    p = 0
    for k in range(k):
        for i in range(p, len(num1) - 1):
            if int(num1[i]) > int(num1[i + 1]):
                num1.remove(num1[i])
                p = i - 1 if i - 1 > 0 else 0
                break
            elif i == len(num1) - 2:
                num1.remove(num1[-1])
                p -= 1
    if len(num1) > 1:
        while num1[0] == '0':
            num1.remove('0')
    elif not num1:
        num1 = ['0']
    else:
        pass
    return ''.join(num1)


# ******************************结束写代码******************************


try:
    _num = input()
except:
    _num = None

_k = int(input())

res = removeKdigits(_num, _k)

print(res + "\n")