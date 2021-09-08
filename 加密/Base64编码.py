# -*- coding:UTF-8 -*-
__author__ = 'rxz'

import base64

a = base64.b64encode(b"hello world")
print(a)  # b'aGVsbG8gd29ybGQ='

b = base64.b64decode(a)
print(b)  # b"hello world"