
url=input().split('?')
del url[0]
url=url[0].split('&')
arr={}
for i in range(len(url)):
    str1=url[i].split('=')
    key=str1[0]
    value=str1[1]
    arr[key]=value
# print(arr)
query=input()
if query in arr:
    print(arr[query])
else:
    print('false')

# https://m.xiaohongshu.com?name=1&id=1
# name