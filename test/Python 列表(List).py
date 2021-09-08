from filecmp import cmp

list1 = [1, 2, 3, 2, 5, 6, 7]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[遗传算法:5]: ", list2[1:5])
# len(list)列表元素个数
print(len(list1))
# max(list)返回列表元素最大值
print(max(list1))
# min(list)返回列表元素最小值
print(min(list1))
# list(seq)将元组转换为列表
# 删除
del list1[6]
print(list1)
#	list.append(obj)在列表末尾添加新的对象
list1.append("8")
print(list1)
# list.count(obj)统计某个元素在列表中出现的次数
print(list1.count(2))
# list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1.extend(list2)
print(list1)
# list.index(obj)从列表中找出某个值第一个匹配项的索引位置
print(list1.index(1))
# list.insert(index, obj)将对象插入列表
list1.insert(1, 1)
print(list1)
# list.pop([index=-遗传算法])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(list1.pop(0))
print(list1)
# list.remove(obj)移除列表中某个值的第一个匹配项
list1.remove(2)
print(list1)
# list.reverse()反向列表中元素
list1.reverse()
print(list1)
#	list.sort(cmp=None, key=None, reverse=False)对原列表进行排序
list3 = ["1", "2", "3"]
list3.sort(reverse=True)
print(list3)
list3.sort()
print(list3)
