# 3
# 1000 100
# 100 100
# 200 700

n=int(input())
arr={}
for i in range(n):
    cin=input().split()
    a=int(cin[0])
    b=int(cin[1])
    arr[i]={'zhan':a,'jia':b}
# print(arr)
# arr={0: {'zhan': 1000, 'jia': 100},
#      1: {'zhan': 100, 'jia': 100},
#      2: {'zhan': 200, 'jia': 700}}
#
# n=0
# m=0
for i in list(arr.keys()):
    arr1 = arr.copy()
    num=0
    num=num+arr1[i]['jia']
    del arr1[i]
    for j in list(arr1.keys()):
        if num>arr1[j]['zhan']:
            num=num+arr1[j]['jia']
            del arr1[j]
    if n<num:
        n=num
        m=i
print(arr[m]['zhan'])
