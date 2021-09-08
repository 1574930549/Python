random = [[90], [60], [90], [70]]
num = random[0][0]
print(num)
for i in range(0, 4):
    for j in range(0, 3 - i):
        if random[j][0] < random[j + 1][0]:
            num = random[j + 1][0]
            random[j + 1][0] = random[j][0]
            random[j][0] = num
random[0].append(1)
for i in range(3):
    if random[i + 1][0] == random[i][0]:
        random[i + 1].append(random[i][1])
    else:
        random[i + 1].append(random[i][1] + 1)
print(random)
