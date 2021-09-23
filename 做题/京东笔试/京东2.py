def huan(a,b):
    if a>b:
        return a,b
    else:
        return b,a
n=int(input())
c=input().split()
num=[]
for i in range(n):
    num.append(int(c[i]))
num=sorted(num)
sum=0
i=0
j=n-1
if n%2==0:
    p=int(n/2)
else:
    p=int(n/2)
    sum =num[j] - num[i]
    j=j-1
    del num[j]
for i in range(p):
    # print(num[j],num[i])
    a,b=huan(num[j],num[i])
    sum = sum + a-b
    j=j-1
print(sum)
