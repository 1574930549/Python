import ast
m = int(input('请输入全部钩码的重量之和的二分之一'))  # 全部钩码的重量之和的二分之一，问题中的n
n = int(input('请输入钩码的数量'))  # 钩码的数量，即题目中的m（个钩码）
a = ast.literal_eval(input("请输入钩码重量，使用逗号隔开: "))
h = [0] * 100
h[0] = 1
for i in range(1, n + 1):
    for j in range(m, 0, -1):
        if j >= a[i - 1]:
            h[j] = h[j] + h[j - a[i - 1]]

for j in range(0, m + 1):
    print(h[j], end=' ')