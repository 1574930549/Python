dict1 = {'遗传算法': 'a', '网页甘特图': 'b', '字符甘特图': 'c'}
dict2 = {'a': '遗传算法', 'b': '网页甘特图', 'c': '字符甘特图'}
print(dict1['遗传算法'])
dict1['网页甘特图'] = 8  # 更新
dict1['自动弹出网页甘特图'] = "d"  # 添加
print(dict1['网页甘特图'])
print(dict1['自动弹出网页甘特图'])
# del dict1['遗传算法']  # 删除键是'Name'的条目
# print(dict1)
# dict1.clear()      # 清空字典所有条目
# print(dict1)
# del dict1          # 删除字典
# print(dict1)

# len(dict)计算字典元素个数，即键的总数。
print('计算字典元素个数，即键的总数', len(dict1))
# str(dict)输出字典可打印的字符串表示。
print('输出字典可打印的字符串表示', str(dict1))
# type(variable)返回输入的变量类型，如果变量是字典就返回字典类型。
print('返回输入的变量类型，如果变量是字典就返回字典类型', type(dict1))
# dict.clear()删除字典内所有元素

# dict.copy()返回一个字典的浅复制
print('返回一个字典的浅复制', dict1.copy())
# dict.fromkeys(seq[, val])创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
seq = ('遗传算法', '网页甘特图', '字符甘特图')
print('创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值', dict1.fromkeys(seq, 2))
# dict.get(key, default=None)返回指定键的值，如果值不在字典中返回default值
print(dict1.get('遗传算法'))
# dict. __contains__(key)如果键在字典dict里返回true，否则返回false
print(dict1. __contains__('网页甘特图'))
# dict.items()以列表返回可遍历的(键, 值) 元组数组
print(dict1.items())
# dict.keys()以列表返回一个字典所有的键
print(dict1.keys())
# dict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
print(dict1.setdefault('遗传算法'))
# dict.update(dict2)把字典dict2的键/值对更新到dict里
print(dict1.update(dict2))
# dict.values()以列表返回字典中的所有值
print(dict1.values())
# pop(key[,default])删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
print(dict1.pop('遗传算法'))
# popitem()返回并删除字典中的最后一对键和值。
print(dict1.popitem())