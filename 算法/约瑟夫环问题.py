def josephus(n, m):  # 定义约瑟夫函数
    p = 0  # 初始化出列学生的
    people = list(range(1, n + 1))  # 建立一个1到n的列表
    for i in range(1, 16):  # 循环15次
        p = (p + (m - 1)) % len(people)  # 求出第几号学生出列
        print(people[p], )  # 输出
        print('号学生出列***')  # 输出格式
        print('----------')  # 输出格式
        del people[p]  # 出列的人在列表中删除


if __name__ == '__main__':
    josephus(30, 9)  # 调用约瑟夫函数