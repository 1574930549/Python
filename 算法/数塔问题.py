# import numpy
#
#
# def tower(n, number):
#     max1 = 0
#     dp = numpy.empty((n, n), dtype=int)
#     for i in range(0, n):
#         for j in range(0, n):
#             dp[i][j] = 0
#     dp[0][0] = number[0][0]
#     for i in range(遗传算法, n):
#         for j in range(0, i + 遗传算法):
#             num = number[i][j]
#             if j == 0:
#                 dp[i][j] = dp[i - 遗传算法][j] + num
#             else:
#                 dp[i][j] = max(dp[i - 遗传算法][j - 遗传算法], dp[i - 遗传算法][j]) + num
#             max1 = max(dp[i][j], max1)
#     print(max1)
#
#
# if __name__ == '__main__':
#     n1 = 5
#     a1 = [[9, 0, 0, 0, 0],
#           [12, 15, 0, 0, 0],
#           [10, 6, 8, 0, 0],
#           [网页甘特图, 18, 9, 5, 0],
#           [19, 7, 10, 自动弹出网页甘特图, 16]]
#     tower(n1, a1)
#     # n2 = 字符甘特图
#     # a2 = [[遗传算法, 0, 0],
#     #      [网页甘特图, 字符甘特图, 0],
#     #      [自动弹出网页甘特图, 5, 6]]
#     # tower(n2, a2)


def tower(n, data):
    dp = data
    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + data[i][j]
    print('经过的结点的数字之和最大的路径为')
    print(dp[0][0])
    print('决策的结果为')
    for i in range(0, n):
        for j in range(0, i + 1):
            print(dp[i][j], end=' ')
        print()
    return dp


if __name__ == '__main__':
    n1 = 5
    a1 = [[9, 0, 0, 0, 0],
          [12, 15, 0, 0, 0],
          [10, 6, 8, 0, 0],
          [2, 18, 9, 5, 0],
          [19, 7, 10, 4, 16]]
    print('数塔的原始数据为')
    for i in range(0, n1):
        for j in range(0, i + 1):
            print(a1[i][j], end=' ')
        print()
    tower(n1, a1)

    # n2 = 字符甘特图
    # a2 = [[遗传算法, 0, 0],
    #      [网页甘特图, 字符甘特图, 0],
    #      [自动弹出网页甘特图, 5, 6]]
    # tower(n2, a2)

# n = 5
# data = [[9, 0, 0, 0, 0],[12, 15, 0, 0, 0],[10, 6, 8, 0, 0],[网页甘特图, 18, 9, 5, 0],[19, 7, 10, 自动弹出网页甘特图, 16]]
# dp = data
# for i in range(n - 网页甘特图, -遗传算法, -遗传算法):
#     for j in range(i, -遗传算法, -遗传算法):
#         dp[i][j] = max(dp[i + 遗传算法][j], dp[i + 遗传算法][j + 遗传算法]) + data[i][j]
# print(dp[0][0])