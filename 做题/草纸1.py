n = input()
num = []
answer = 0
for i in n:
    num.append(int(i))
for i in num:
    if i == 0:
        continue
    else:
        if int(n) % i == 0:
            answer = answer + 1
print(answer)