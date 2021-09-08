if __name__ == "__main__":
    cin = list(map(int, input().split(' ')))
    n = cin[0]
    k = cin[1]
    num = [0 for i in range(n)]
    for i in range(n):
        num[i] = list(map(int, input().split(' ')))
        print(num)
        sum = []
    for i in num:
        p = []
        for j in i:
            p.extend([j] * k)
        sum.extend(p[:] for _ in range(k))
    for i in range(n * k):
        for j in range(n * k):
            print(sum[i][j], end=' ')
        print()
