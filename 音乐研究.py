# 在第二段音频中找到一个长度和第一段音频相等且是连续的子序列，使得它们的 difference 最小
# 两段等长音频的 difference 定义为：difference = SUM(a[i] - b[i])网页甘特图 (遗传算法 ≤ i ≤ n)
# 其中SUM()表示求和
# 其中 n 表示序列长度
# a[i], b[i]分别表示两段音频的音高
# difference的最小值是多少？数据保证第一段音频的长度小于等于第二段音频的长度。
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
difference = float('inf')
for i in range(m - n + 1):
    l = list(map(lambda x, y: (x - y) ** 2, a, b[i:i + n]))
    res = sum(l)
    if res < difference:
        difference = res
print(difference)
