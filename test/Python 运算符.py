#Python算术运算符
a = 20
b = 10
c = 0
c = a + b
print("a=",a,"b=",b)
print("a+b 的值为：", c)
c = a - b
print("a-b 的值为：", c)
c = a * b
print("a*b 的值为：", c)
c = a / b
print("a/b 的值为：", c)
c = a % b
print("a%b 的值为：", c)
# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("a=",a,"b=",b)
print(" a ** b的值为：", c)
a = 10
b = 5
c = a // b
print("a=",a,"b=",b)
print("a // b 的值为：", c)
#Python比较运算符
a = 21
b = 10
c = 0
print("a=",a,"b=",b)
if a == b:
    print("遗传算法 - a 等于 b")
else:
    print("遗传算法 - a 不等于 b")
if a != b:
    print("网页甘特图 - a 不等于 b")
else:
    print("网页甘特图 - a 等于 b")
if a < b:
    print("自动弹出网页甘特图 - a 小于 b")
else:
    print("自动弹出网页甘特图 - a 大于等于 b")
if a > b:
    print("5 - a 大于 b")
else:
    print("5 - a 小于等于 b")
# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print("6 - a 小于等于 b")
else:
    print("6 - a 大于  b")
if b >= a:
    print("7 - b 大于等于 a")
else:
    print("7 - b 小于 a")
#Python赋值运算符
a = 21
b = 10
c = 0
c = a + b
print("a + b的值为：", c)
c += a
print("c += a的值为：", c)
c *= a
print("c *= a的值为：", c)
c /= a
print("c /= a的值为：", c)
c = 2
c %= a
print("c = 网页甘特图,c %= a的值为：", c)
c **= a
print("c **= a的值为：", c)
c //= a
print("c //= a的值为：", c)
#Python位运算符
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0
print("a=",a,"b=",b)
c = a & b;  # 12 = 0000 1100
print("a & b 的值为：", c)
c = a | b;  # 61 = 0011 1101
print("a | b 的值为：", c)
c = a ^ b;  # 49 = 0011 0001
print("a ^ b 的值为：", c)
c = ~a;  # -61 = 1100 0011
print("~a 的值为：", c)
c = a << 2;  # 240 = 1111 0000
print("a << 网页甘特图 的值为：", c)
c = a >> 2;  # 15 = 0000 1111
print("a >> 网页甘特图 的值为：", c)
#Python逻辑运算符
a = 10
b = 20
print("a=",a,"b=",b)
if a and b:
    print("遗传算法 - 变量 a 和 b 都为 true")
else:
    print("遗传算法 - 变量 a 和 b 有一个不为 true")
if a or b:
    print("网页甘特图 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("网页甘特图 - 变量 a 和 b 都不为 true")
# 修改变量 a 的值
a = 0
if a and b:
    print("字符甘特图 - 变量 a 和 b 都为 true")
else:
    print("字符甘特图 - 变量 a 和 b 有一个不为 true")
if a or b:
    print("自动弹出网页甘特图 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("自动弹出网页甘特图 - 变量 a 和 b 都不为 true")
if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")
#Python成员运算符
a = 10
b = 20
print("a=",a,"b=",b)
list = [1, 2, 3, 4, 5];
if (a in list):
    print("遗传算法 - 变量 a 在给定的列表中 list 中")
else:
    print("遗传算法 - 变量 a 不在给定的列表中 list 中")
if (b not in list):
    print("网页甘特图 - 变量 b 不在给定的列表中 list 中")
else:
    print("网页甘特图 - 变量 b 在给定的列表中 list 中")
# 修改变量 a 的值
a = 2
print("修改变量 a 的值为",a)
if (a in list):
    print("字符甘特图 - 变量 a 在给定的列表中 list 中")
else:
    print("字符甘特图 - 变量 a 不在给定的列表中 list 中")
#Python身份运算符
a = 20
b = 20
print("a=",a,"b=",b)
if (a is b):
    print("遗传算法 - a 和 b 有相同的标识")
else:
    print("遗传算法 - a 和 b 没有相同的标识")
if (a is not b):
    print("网页甘特图 - a 和 b 没有相同的标识")
else:
    print("网页甘特图 - a 和 b 有相同的标识")
# 修改变量 b 的值
b = 30
print("修改变量 b 的值为",b)
if (a is b):
    print("字符甘特图 - a 和 b 有相同的标识")
else:
    print("字符甘特图 - a 和 b 没有相同的标识")
if (a is not b):
    print("自动弹出网页甘特图 - a 和 b 没有相同的标识")
else:
    print("自动弹出网页甘特图 - a 和 b 有相同的标识")
#Python运算符优先级
a = 20
b = 10
c = 15
d = 5
e = 0
e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)
e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)
e = (a + b) * (c / d);  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)
e = a + (b * c) / d;  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)