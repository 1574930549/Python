
num=[{'a': 20, 'b': 1000, 'c': 1, 'd': 2}, {'a': 1, 'b': 1, 'c': 1, 'd': 1}, {'a': 5, 'b': 3, 'c': 1, 'd': 3}, {'a': 20, 'b': 1, 'c': 2, 'd': 2}, {'a': 22, 'b': 2, 'c': 2, 'd': 3}]
print(num)
num=sorted(num,key=lambda x:x['d'])
print(num)
ans=0
for i in num:
    print(i)