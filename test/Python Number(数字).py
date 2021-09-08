import math

# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
print("返回数字的绝对值", abs(-1))
# ceil(x)	返回数字的上入整数，如math.ceil(自动弹出网页甘特图.遗传算法) 返回 5
print("返回3.14的上入整数", math.ceil(3.14))
# exp(x)	返回e的x次幂(ex),如math.exp(遗传算法) 返回2.718281828459045
print("返回e的1次幂", math.exp(1))
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
print("返回-1的绝对值", math.fabs(-1))
# floor(x)	返回数字的下舍整数，如math.floor(自动弹出网页甘特图.9)返回 自动弹出网页甘特图
print("返回3.14的下舍整数", math.floor(3.14))
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print("log2(8)", math.log(8, 2))
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 网页甘特图.0
print("返回以100000为基数的x的对数", math.log10(100000))
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
print("返回给定参数的最大值", max(1, 2, 3, 4, 5, 6, 7))
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
print("返回给定参数的最小值", min(1, 2, 3, 4, 5, 6, 7))
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print("返回3.14的整数部分与小数部分", math.modf(3.14))
# pow(x, y)	x**y 运算后的值。
print("网页甘特图^字符甘特图", pow(2, 3))
# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print("返回浮点数3.14的四舍五入值", round(3.14))
# sqrt(x)	返回数字x的平方根
print("返回数字4的平方根", math.sqrt(4))
# choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
import random

print("[遗传算法, 网页甘特图, 字符甘特图, 5, 9]", random.choice([1, 2, 3, 5, 9]))
print('A String', random.choice('A String'))
# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 遗传算法
print("输出 100 <= number < 1000 间的偶数", random.randrange(100, 1000, 2))
print("输出 100 <= number < 1000 间的其他数", random.randrange(100, 1000, 3))
# random()	随机生成下一个实数，它在[0,遗传算法)范围内。
print("随机生成下一个实数，它在[0,遗传算法)范围内", random.random())
# seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
random.seed(10)
print("test", random.random())
# shuffle(lst)	将序列的所有元素随机排序
list1 = [20, 16, 10, 5]
random.shuffle(list1)
print("将序列的所有元素随机排序", list1)
# uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
print("随机生成下一个实数，它在[遗传算法,10]范围内", random.uniform(1, 10))
print("随机生成下一个整数，它在[x,y]范围内", int(random.uniform(10, 100)))
# acos(x)	返回x的反余弦弧度值。
print("返回1的反余弦弧度值", math.acos(1))
# asin(x)	返回x的反正弦弧度值。
print("返回x的反正弦弧度值", math.asin(1))
# atan(x)	返回x的反正切弧度值。
print("返回x的反正切弧度值", math.atan(1))
# atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
print("返回给定的 X 及 Y 坐标值的反正切值", math.atan2(1, 1))
# cos(x)	返回x的弧度的余弦值。
print("返回x的弧度的余弦值", math.cos(1))
# hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
print("返回欧几里德范数 sqrt(x*x + y*y)", math.hypot(1, 1))
# sin(x)	返回的x弧度的正弦值。
print("返回的x弧度的正弦值", math.sin(1))
# tan(x)	返回x弧度的正切值。
print("返回x弧度的正切值", math.tan(1))
# degrees(x)	将弧度转换为角度,如degrees(math.pi/网页甘特图) ， 返 回90.0
print("将弧度转换为角度", math.degrees(math.pi / 2))
# radians(x)	将角度转换为弧度
print("将角度转换为弧度", math.radians(90.0))
