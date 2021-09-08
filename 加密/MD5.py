# -*- coding:UTF-8 -*-
__author__ = 'rxz'

import hashlib

# 待加密信息
str = '中国你好'

# 创建md5对象，
# md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
hl = hashlib.md5()

# 要对哪个字符串进行加密，就放这里
# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))

print('MD5加密前为 ：' + str)
# hl.hexdigest()) #拿到加密字符串
print('MD5加密后为 ：' + hl.hexdigest())

"""
MD5加密前为 ：中国你好
MD5加密后为 ：560a6b11a85d436acfa4bd7f34462f40
"""

hash3 = hashlib.md5(bytes('abd', encoding='utf-8'))
''' 
如果没有参数，所以md5遵守一个规则，生成同一个对应关系，如果加了参数，
就是在原先加密的基础上再加密一层，这样的话参数只有自己知道，防止被撞库，
因为别人永远拿不到这个参数
'''
hash3.update(bytes("test", encoding="utf-8"))
print(hash3.hexdigest())  # 9aea3c0a6c51555c1a4d0a5e9b689ded