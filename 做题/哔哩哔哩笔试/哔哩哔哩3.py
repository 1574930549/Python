n = int(input())
num = 0
for i in range(n+1):
    if i % 2 == 0:
        continue
    else:
        num = num + i
print(num)
