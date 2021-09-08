def gcd(a, b):
    # if a < b:
    #     a, b = b, a
    # else:
    #     return gcd(b,a%b)
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a / gcd(a, b) * b;


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        num = []
        for j in range(1, int(n / 2)):
            for k in range(int(n / 2), n):
                if gcd(j, k) == 1:
                    if lcm(j, k) == j * k:
                        if j in num:
                            break
                        else:
                            num.append(j)

        print(len(num))
