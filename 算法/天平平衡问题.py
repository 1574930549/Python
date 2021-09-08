def tianping(m, n, a):
    h = [0] * 100
    h[0] = 1
    for i in range(1, n + 1):
        for j in range(m, 0, -1):
            if j >= a[i - 1]:
                h[j] = h[j] + h[j - a[i - 1]]

    for j in range(0, m + 1):
        print(h[j], end=' ')
    return h


if __name__ == '__main__':
    m1 = 27  # 全部钩码的重量之和的二分之一，问题中的n
    n1 = 9  # 钩码的数量，即题目中的m（个钩码）
    a1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    print('m1=', m1)
    print('n1=', n1)
    print('a1=', a1)
    print('运行结果为：')
    tianping(m1, n1, a1)
    print()
    m2 = 10
    n2 = 4
    a2 = [7, 6, 4, 3]
    print('m2=', m2)
    print('n2=', n2)
    print('a2=', a2)
    print('运行结果为：')
    tianping(m2, n2, a2)


# import ast
# m = int(input('请输入全部钩码的重量之和的二分之一'))  # 全部钩码的重量之和的二分之一，问题中的n
# n = int(input('请输入钩码的数量'))  # 钩码的数量，即题目中的m（个钩码）
# a = ast.literal_eval(input("请输入钩码重量，使用逗号隔开: "))
# h = [0] * 100
# h[0] = 遗传算法
# for i in range(遗传算法, n + 遗传算法):
#     for j in range(m, 0, -遗传算法):
#         if j >= a[i - 遗传算法]:
#             h[j] = h[j] + h[j - a[i - 遗传算法]]
#
# for j in range(0, m + 遗传算法):
#     print(h[j], end=' ')