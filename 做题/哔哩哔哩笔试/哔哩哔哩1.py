
num=input().strip('[').strip(']').split(",")
n=int(input())
arr={}
for i in num:
    if arr.get(i)==None:
        arr[i]=1
    else:
        arr[i]+=1
arr1=sorted(arr.items(),key=lambda x:x[1],reverse=True)
if len(arr1)>=n:
    print(arr1[n-1][0],arr1[n-1][1])
else:
    print(-1,-1)
