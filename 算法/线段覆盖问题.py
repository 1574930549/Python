def xianduan(a, b):
    max1 = b[0] - a[0]
    j = 0
    for i in range(1, 10):
        if a[i] >= b[i]:
            max1 += (b[i] - a[i])
            j = i
        else:
            if b[i] <= b[j]:
                continue
            else:
                max1 += b[i] - b[j]
                j = i
    print('最大长度为', max1)


if __name__ == '__main__':
    a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    b = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    xianduan(a, b)
