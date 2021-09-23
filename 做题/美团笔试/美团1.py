# 被22整除的子字符串数
str1=input()
long=len(str1)

s=[str1[i:i+x+1]for x in range(len(str1))for i in range(len(str1)-x)]

# print(s)
num=0
for i in s:
    if int(i)%22==0:
        num=num+1
print(num)