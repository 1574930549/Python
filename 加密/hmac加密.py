import hmac

hm = hmac.new(b'abc')
hm = hmac.new('中国你好'.encode(encoding='utf-8'), b'bads')
print(hm.digest())
print(hm.hexdigest())

"""
b'\xc8;\x0c\x0b\xd42\xc37\xd0X\xbc\xfbf=RP'
c83b0c0bd432c337d058bcfb663d5250
"""