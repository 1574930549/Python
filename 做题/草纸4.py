# 2 5 10
# *#
# #*

# 4 5 10
# ....
# .##.
# .##.
# ....

cin=input().split()
n=int(cin[0])
a=int(cin[1])
b=int(cin[2])
str1=[]
for i in range(n):
    str1.append(input())
for i in range(len(str1)):
    p=str1[i]
    str1[i]=[]
    for j in range(len(p)):
        str1[i].append(p[j])
# n=4
# a=5
# b=10
# str1=[['.', '.', '.', '.'], ['.', '#', '#', '.'], ['.', '#', '#', '.'], ['.', '.', '.', '.']]
for i in range(len(str1)):
    for j in range(len(str1)):
        if str1[i][j]=='.':
            str1[i][j]=0
        elif str1[i][j]=='#':
            str1[i][j]=a
        else:
            str1[i][j]=b/2
go=[(0, 1), (1, 0), (0, -1), (-1, 0)]

