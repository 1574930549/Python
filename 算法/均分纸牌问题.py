def zhipai(n):
    sum1 = 0
    count = 0
    # a = [1] * 100
    a = [9, 8, 17, 6]
    for i in range(0, n):
        # a[i] = int(input())
        sum1 = sum1 + a[i]
        # print(sum1)
    average = int(sum1 / n)
    # print(average)
    for i in range(0, n):
        a[i] -= average
        # print(a[i])
    for i in range(0, n):
        if a[i] != 0:
            a[i + 1] = a[i + 1] + a[i]
            count = count + 1
            a[i] = 0
            # print(count)
    print(count)


if __name__ == '__main__':
    # n = int(input())
    n = 4
    zhipai(n)
