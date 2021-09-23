str1=input()
cin=input().split()
a=int(cin[0])
b=int(cin[1])

# str1='IBBPIPPPPP'
# a=0
# b=5
str2=str1[a:b]
# print(str2)
str3=str2.split('I')
str3=[i for i in str3 if i !='']
if str2[0]=="I":
    pass
else:
    del str3[0]

if len(str2)==len(str1) :
    pass
else:
    if str2[len(str2)-1] in ["B", "P"] and str1[len(str2)] in ["B", "P"] :
        del str3[len(str3) - 1]
# print(str3)
for i in str3:
    print("I"+i)