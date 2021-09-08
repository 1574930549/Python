# # -*- coding:UTF-8 -*-
# __author__ = 'rxz'
#
# import rsa
#
#
# # rsa加密
# def rsaEncrypt(str):
#     # 生成公钥、私钥
#     (pubkey, privkey) = rsa.newkeys(512)
#     print("pub: ", pubkey)
#     print("priv: ", privkey)
#     # 明文编码格式
#     content = str.encode('utf-8')
#     # 公钥加密
#     crypto = rsa.encrypt(content, pubkey)
#     return (crypto, privkey)
#
#
# # rsa解密
# def rsaDecrypt(str, pk):
#     # 私钥解密
#     content = rsa.decrypt(str, pk)
#     con = content.decode('utf-8')
#     return con
#
#
# (a, b) = rsaEncrypt("hello")
# print('加密后密文：')
# print(a)
# print(b)
# content = rsaDecrypt(a, b)
# print('解密后明文：')
# print(content)
# -*- coding:UTF-8 -*-
__author__ = 'rxz'

import rsa
import binascii


def rsa_encrypt(rsa_n, rsa_e, message):
    key = rsa.PublicKey(rsa_n, rsa_e)
    message = rsa.encrypt(message.encode(), key)
    message = binascii.b2a_hex(message)
    return message.decode()


pubkey_n = '8d7e6949d411ce14d7d233d7160f5b2cc753930caba4d5ad24f923a505253b9c39b09a059732250e56c594d735077cfcb0c3508e9f544f101bdf7e97fe1b0d97f273468264b8b24caaa2a90cd9708a417c51cf8ba35444d37c514a0490441a773ccb121034f29748763c6c4f76eb0303559c57071fd89234d140c8bb965f9725'
pubkey_e = '10001'
rsa_n = int(pubkey_n, 16)
rsa_e = int(pubkey_e, 16)
message = '南北今天很忙'
print("公钥n值长度：", len(pubkey_n))

aa = rsa_encrypt(rsa_n, rsa_e, message)
print(aa)