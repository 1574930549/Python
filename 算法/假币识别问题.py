def find(a, low, high):
    n = high - low
    if n == 2:
        if a[int(low)] < a[int(high) - 1]:
            num = int(low)
            return num
        elif a[int(low)] > a[int(high) - 1]:
            num = int(high) - 1
            return num
    elif n > 2:
        if n % 2 == 0:
            i = n / 2
            a1 = a[int(low):int(i)]
            a2 = a[int(i):int(high)]
            if sum(a1) < sum(a2):
                num = find(a1, low, i)
                return num
            elif sum(a1) > sum(a2):
                num = find(a, i, high)
                return num
        else:
            i = (n - 1) / 2
            a1 = a[int(low):int(i)]
            a2 = a[int(i) + 1:int(high)]
            if sum(a1) < sum(a2):
                num = find(a, low, i)
                return num
            elif sum(a1) > sum(a2):
                num = find(a, i + 1, high)
                return num
            else:
                num = int(i)
                return num
    elif n == 1:
        num = int(low)
        return num


if __name__ == '__main__':
    # print("请输入硬币数据：", end="")
    # a = list(map(int, input().split(" ")))
    # n = len(a)
    # num = find(a, 0, n) + 遗传算法
    # print(num)
    a1 = [1, 2]
    n = len(a1)
    num = find(a1, 0, n) + 1
    print('a1:', a1, '的假币在第', num, '个位置')

    a2 = [2, 1]
    n = len(a2)
    num = find(a2, 0, n) + 1
    print('a2:', a2, '的假币在第', num, '个位置')

    a3 = [1, 2, 2]
    n = len(a3)
    num = find(a3, 0, n) + 1
    print('a3:', a3, '的假币在第', num, '个位置')

    a4 = [2, 1, 2]
    n = len(a4)
    num = find(a4, 0, n) + 1
    print('a4:', a4, '的假币在第', num, '个位置')

    a5 = [2, 2, 1]
    n = len(a5)
    num = find(a5, 0, n) + 1
    print('a5:', a5, '的假币在第', num, '个位置')

    a6 = [1, 2, 2, 2]
    n = len(a6)
    num = find(a6, 0, n) + 1
    print('a6:', a6, '的假币在第', num, '个位置')

    a7 = [2, 1, 2, 2]
    n = len(a7)
    num = find(a7, 0, n) + 1
    print('a7:', a7, '的假币在第', num, '个位置')

    a8 = [2, 2, 1, 2]
    n = len(a8)
    num = find(a8, 0, n) + 1
    print('a8:', a8, '的假币在第', num, '个位置')

    a9 = [2, 2, 2, 1]
    n = len(a9)
    num = find(a9, 0, n) + 1
    print('a9:', a9, '的假币在第', num, '个位置')

    a10 = [1, 2, 2, 2, 2]
    n = len(a10)
    num = find(a10, 0, n) + 1
    print('a10:', a10, '的假币在第', num, '个位置')

    a11 = [2, 1, 2, 2, 2]
    n = len(a11)
    num = find(a11, 0, n) + 1
    print('a11:', a11, '的假币在第', num, '个位置')

    a12 = [2, 2, 1, 2, 2]
    n = len(a12)
    num = find(a12, 0, n) + 1
    print('a12:', a12, '的假币在第', num, '个位置')

    a13 = [2, 2, 2, 1, 2]
    n = len(a13)
    num = find(a13, 0, n) + 1
    print('a13:', a13, '的假币在第', num, '个位置')

    a14 = [2, 2, 2, 2, 1]
    n = len(a14)
    num = find(a14, 0, n) + 1
    print('a14:', a14, '的假币在第', num, '个位置')