def Binarysearch(arr, find):
    long = len(arr)
    first = 0
    last = long - 1
    while first < last:
        mid = (last + first) // 2
        if arr[mid] > find:
            last = mid
        elif arr[mid] < find:
            first = mid + 1
        else:
            return mid


if __name__ == '__main__':
    print("请输入数组数据：", end="")
    arr = list(map(int, input().split(" ")))
    arr.sort()  # 排序
    print("你输入的数组为：", end="")
    print(arr)
    long = len(arr)  # 长度
    print("请输入您要查找的数字：")
    find = int(input())
    if find in arr:
        x = Binarysearch(arr, find)
        print("数字存在数组当中！数组下标为：", x)
    else:
        print("你要找的数字不在这个列表里！")
        if max(arr) < find:
            print("没有比你查找数字更大的了！")
            print("比查找数字小的最大数组元素下标为", long - 1)
        elif min(arr) > find:
            print("没有比查找数字还小的了！")
            print("比查找数字大的最小数组元素下标为0")
        else:
            for y in range(0, long):
                if arr[y] < find:
                    y += 1
                else:
                    print("比寻找数字大的下标为", y)
                    print("比寻找数字小的下标为", y - 1)
                    break
