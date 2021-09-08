import math
from random import randrange, random


A=[[0 for i in range(6)]for i in range(10)]
B = [[0 for i in range(6)]for i in range(10)]
C = [[0 for i in range(6)]for i in range(10)]
for i in range(0, 10):
    for j in range(0, 6):
        if random() < 0.5:
            A[i][j] = 0
        else:
            A[i][j] = 1
        B[i][j] = randrange(0, 10)
        C[i][j] = randrange(0, 10)


def Smc(f00, f01, f10, f11):
    smc = [[0 for i in range(10)]for i in range(10)]
    smc1 = [[0 for i in range(10)]for i in range(10)]
    for j in range(0, 10):
        for i in range(0, 10):
            smc[j][i] = (f11[j][i] + f00[j][i])
            smc1[j][i] = smc[j][i] / (f01[j][i] + f10[j][i] + f11[j][i] + f00[j][i])
    return smc1


def distB():
    sumb =[[0 for i in range(10)]for i in range(10)]
    sb = [[1 for i in range(10)]for i in range(10)]
    distb = [[0 for i in range(10)]for i in range(10)]
    for n in range(0, 10):
        for xb in range(0, 10):
            for yb in range(0, 6):
                sumb[n][xb] = sumb[n][xb] + (B[n][yb] - B[xb][yb]) * (B[n][yb] - B[xb][yb])
            # print(sumb)
            distb[n][xb] = math.sqrt(sumb[n][xb])
            # print(distb)
            sb[n][xb] = sb[n][xb] / (1 + distb[n][xb])
    return sb


def smcC():
    sumc1 = [[0 for i in range(10)]for i in range(10)]
    sumc2 = [[0 for i in range(10)]for i in range(10)]
    sumc3 = [[0 for i in range(10)]for i in range(10)]
    sumc = [[0 for i in range(10)]for i in range(10)]
    sum = [[0 for i in range(10)]for i in range(10)]

    for n in range(0, 10):
        for xc in range(0, 10):
            for yc in range(0, 6):
                sumc1[n][xc] = sumc1[n][xc] + C[n][yc] * C[xc][yc]
            for yc in range(0, 6):
                sumc2[n][xc] = sumc2[n][xc] + C[n][yc] * C[n][yc]
            for yc in range(0, 6):
                sumc3[n][xc] = sumc3[n][xc] + C[xc][yc] * C[xc][yc]
            sumc[n][xc] = math.sqrt(sumc2[n][xc]) * math.sqrt(sumc3[n][xc])
            sum[n][xc] = sumc1[n][xc] / sumc[n][xc]
    return sum


def Sim(a, b, c, wa, wb, wc):
    sim = [[0 for i in range(10)]for i in range(10)]

    for n in range(0, 10):
        for i in range(0, 10):
            sim[n][i] = wa * a[n][i] + wb * b[n][i] + wc * c[n][i]
    return sim


def f():
    f00 = [[0 for i in range(10)]for i in range(10)]
    f01 = [[0 for i in range(10)]for i in range(10)]
    f10 = [[0 for i in range(10)]for i in range(10)]
    f11 = [[0 for i in range(10)]for i in range(10)]

    for n in range(0, 10):
        for j in range(0, 10):
            for i in range(0, 6):
                if (A[n][i] == A[j][i]) & A[n][i] == 0:
                    f00[n][j] = f00[n][j] + 1

            for i in range(0, 6):
                if (A[n][i] != A[j][i]) & A[n][i] == 0 & A[j][i] == 1:
                    f01[n][j] = f01[n][j] + 1
            # print(f01)
            for i in range(0, 6):
                if (A[n][i] != A[j][i]) & A[n][i] == 1:
                    f10[n][j] = f10[n][j] + 1
            # print(f10)
            for i in range(0, 6):
                if (A[n][i] == A[j][i]) & A[n][i] == 1:
                    f11[n][j] = f11[n][j] + 1
            # print(f11)
    # print(f00)
    # print(f01)
    # print(f10)
    # print(f11)
    return f00, f01, f10, f11

def out(e):
    for i in range(0,10):
        for j in range(0,10):
            print('%-10f' % (e[i][j]),end=" ")
        print()

if __name__ == "__main__":
    f00, f01, f10, f11 = f()
    sA = Smc(f00, f01, f10, f11)
    print("简单匹配系数度量相似性")
    out(sA)
    sB = distB()
    print("欧式距离度量距离")
    out(sB)
    sC = smcC()
    print("余弦距离度量相似性")
    out(sC)
    sim = Sim(sA, sB, sC, 0.3, 0.2, 0.5)
    print("相似性")
    out(sim)
