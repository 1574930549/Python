n=int(input())
num=[]
num2=bin(n)[:1:-1]
num3=[]
for i in range(len(num2)):
    if int(num2[i]):
        num.append(2**i)
    else:
        num3.append(2**i)
if num==[] and num3==[1]:
    print(-1)
else:
    if len(num)<=len(num3):
        print(len(num))
    else:
        print(len(num3)+1)