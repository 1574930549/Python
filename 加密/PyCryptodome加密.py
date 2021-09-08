# # -*- coding:UTF-8 -*-
# __author__ = 'rxz'
#
# # 导入DES模块
# from Cryptodome.Cipher import DES
# import binascii
#
# # 这是密钥,此处需要将字符串转为字节
# key = b'abcdefgh'
#
#
# # 需要去生成一个DES对象
# def pad(text):
#     """
#       # 加密函数，如果text不是8的倍数【加密文本text必须为8的倍数！】，那就补足为8的倍数
#        :param text:
#        :return:
#     """
#     while len(text) % 8 != 0:
#         text += ' '
#     return text
#
#
# # 创建一个DES实例
# des = DES.new(key, DES.MODE_ECB)
# text = "I'm china!"
# padded_text = pad(text)
# print(padded_text)
# # 加密
# encrypted_text = des.encrypt(padded_text.encode("utf-8"))
# print(encrypted_text)
# # rstrip(' ')返回从字符串末尾删除所有字符串的字符串(默认空白字符)的副本
#
# # 解密
# plain_text = des.decrypt(encrypted_text).decode().rstrip(' ')
# print(plain_text)
#
# """
# I'm china!
# b'\xc0`I\x15\x8bo\x00\x00\xb0\xe27\xfe)\xc3\xde,'
# I'm china!
# """
#
#
#
# -*- coding:UTF-8 -*-
__author__ = 'rxz'

# 导入DES模块
from Cryptodome.Cipher import DES
import binascii

# 这是密钥
key = b'abcdefgh'
# 需要去生成一个DES对象
des = DES.new(key, DES.MODE_ECB)
# 需要加密的数据
text = 'python spider!'
text = text + (8 - (len(text) % 8)) * '='
# 加密的过程
encrypto_text = des.encrypt(text.encode())
# 加密过后二进制转化为ASCII
encrypto_text = binascii.b2a_hex(encrypto_text)
print(encrypto_text)
# 解密需要ASCII 先转化为二进制 然后再进行解密
plaint = des.decrypt(binascii.a2b_hex(encrypto_text))
print(plaint)

"""
b'084725d8f5ffafc61814fae0796bfd2f'
b'python spider!=='
"""
