# 给定两个整数 l 和 r
# 对于所有满足1 ≤ l ≤ x ≤ r ≤ 10^9 的 x
# 把 x 的所有约数全部写下来
# 对于每个写下来的数，只保留最高位的那个数码
# 求1～9每个数码出现的次数。


def yue(mm, pp):
    num = 0
    for x in range(1, mm + 1):
        for i in range(1, x + 1):
            if x % i == 0:
                j = sm(i)
                if j == pp:
                    num = num + 1
    return num


def sm(jj):
    for j in str(jj):
        j = int(j)
        return j


n, m = [int(j) for j in input().split()]
for p in range(1, 10):

    print(yue(m, p)-yue(n-1,p))
