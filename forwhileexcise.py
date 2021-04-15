from collections import defaultdict
'''
内置函数id()查看当前对象的内存地址，None值也有内存地址

'''

# attributes = ['name', 'dob', 'gender']
#
# values = [
#     ['jason', '2000-1-1', 'male1'],
#     ['mike', '2001-2-2', 'male2'],
#     ['nancy', '2002-3-3', 'female3']
# ]
#
# l = []
#
# for j, v2 in enumerate(values):
#     dis = {}
#     print(id(dis))
#     for i in range(len(v2)):
#         dis[attributes[i]] = v2[i]
#     l.append(dis)
#
# # l = [l.append({v3: v2}) for i in values for j, v2 in enumerate(i) for k, v3 in enumerate(attributes) if k == j]
#
# # l=[{attributes[i]:v[i]} for j,v in enumerate(values) for i in range(len(v))]
# print(l)

# print([dict(zip(attributes,v)) for v in values])

"""
zip(iterable,,,)
内置函数，将一个或者多个迭代器对应的元素打包成一个个元组，返回值为一个个元组组成的列表，<zip object at 0x000001776CBDF788>
如果多个迭代器中的元素数目不同，则返回列表长度与最短对象相同
将元组解压为列表，用*
"""

a = [1, 2, 3]
b = {4, 5, 6}
c = (7, 8, 9)
d = [9,8,7,6,5]
f=zip(a,d)

print(zip(*f))

