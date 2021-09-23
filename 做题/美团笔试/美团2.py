cin=input().split()
n=int(cin[0])
m=int(cin[1])
q=int(cin[2])
# n=5
# m=5
# q=3
num={}
for i in range(1,n+1):
    num.setdefault(i,0)
for i in range(m):
    cin2=input().split()
    p1=int(cin2[0])
    p2=int(cin2[1])
    num[p1]=num[p1]+1
    num[p2]=num[p2]+1
# print(num)
# num={1:2,2:2,3:2,4:3,5:1}
for i in range(q):
    cin3=input().split()
    p3 = int(cin3[0])
    p4 = int(cin3[1])
    t1=num.get(p3)
    t2=num.get(p4)
    # print(t1,t2)
    w1={p3:t2}
    w2={p4:t1}
    num.update(w1)
    num.update(w2)
# print(num)
for i in num:
    print(num[i],end=' ')

# 5 5 3
# 1 2
# 2 3
# 3 4
# 4 5
# 1 4
# 5 2
# 1 2
# 3 4