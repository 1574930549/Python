for i in 'Python':  # 第一个实例
    print('当前字母 :', i)

fruits = ['banana', 'apple', 'mango']
for j in fruits:  # 第二个实例
    print('当前水果 :', j)

fruits = ['banana', 'apple', 'mango']
for p in range(len(fruits)):
    print('当前水果 :', fruits[p])

print("Good bye!")
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')
