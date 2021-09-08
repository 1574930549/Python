def abc(num):
    a = num % 10
    b = int(num / 10) % 10
    c = int(num / 100) % 10
    if a in [1, 2, 3]:
        if b in [1, 2, 3]:
            if c in [1, 2, 3]:
                return 1
            else:
                return 2
        else:
            return 2
    else:
        return 2


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        for j in range(n, 0, -1):
            if abc(j) == 1:
                print(j)
                break
