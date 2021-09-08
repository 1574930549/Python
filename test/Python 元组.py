tup1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
tup3 = tup1 + tup2
print(tup3)
del tup3
print("After deleting tup : ")
# print(tup3)
# len(tuple)计算元组元素个数。
print(len(tup1))
# max(tuple)返回元组中元素最大值。
print(max(tup1))
# min(tuple)返回元组中元素最小值。
print(min(tup1))
# tuple(seq)将列表转换为元组。
list1 = [1, 2, 3, 2, 5, 6, 7]
tup3 = tuple(list1)
print(tup3)
