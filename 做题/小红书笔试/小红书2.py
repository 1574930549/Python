n=input().replace('[','').replace(']','').split(',')
for i in range(len(n)):
    n[i]=int(n[i])
if len(n)==0 or len(n)==1:
    print(0)
else:
    num1=0
    num2=n[0]
    for i in range(1,len(n)):
        num1=max(n[i]-num2,num1)
        num2=min(n[i],num2)
    print(num1)