var1 = 'zhanglihui'
for i in range(1, 11):  # 1到10层
    for j in range(0, 20):  # 1到20列
        if j < 10 - i:  # 如果列数小于10减去行数（金字塔之前空白区域部分）
            print(" ", end=' ')  # 输出空格占位
        if j >= 10 - i:  # 如果列数大于等于10减去行数
            if j < 10:  # 并且列数小于10（金字塔塔尖往左部分）
                print(var1[9 - j], end=' ')  # 如果在前半段字符串为倒序
        if j > 10:  # 如果列数大于等于10
            if j < i + 10:  # 并且列数小于10加上行数（金字塔塔尖往右部分）
                print(var1[j - 10], end=' ')  # 如果在后半段字符串为正序
    print()  # 每输出一行进行换行
