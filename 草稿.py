a=[[0,0,0,0,0,0,],[0,0,0,0,0,0,],[0,0,0,0,0,0,],[0,0,0,0,0,0,],[0,0,0,0,0,0,],[0,0,0,0,0,0,],[0,0,0,0,0,0,],[0,0,0,0,0,0,]]
for  i in range(3,7):
    for j in range(2,i-1):
        print(j,end="")
    print()
for i in range(1,7):
    for j in range(i):
        print(a[i][j],end="")
    print()