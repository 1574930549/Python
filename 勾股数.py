n = 0
for a in range(3, 50):
    for b in range(a + 1, 50):
        for c in range(b + 1, 50):
            if a ** 2 + b ** 2 == c ** 2:
                print(a, ',', b, ',', c, '   ', end=' ')
                n += 1
                if n == 6:
                    print()
                    n = 0
