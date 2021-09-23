str1=input()
# str1='AAAABBBCCDAABBB'
str2=[""]
for i in str1:
    if i == str2[-1]:
        continue
        # str2.pop()
        # str2.append(i)
    else:
        str2.append(i)
print(''.join(str2))