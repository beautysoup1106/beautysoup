from functools import reduce
'''
1.map函数在2.X版本返回的是一个列表，在3.X返回的是map类，一个迭代器
2.filter函数在2.X版本过滤后返回过滤后的列表，3.X返回的是一个filter类，一个迭代器
3.reduce函数在3.X中非内建函数，被放置在functools模块里，使用时需要导入模块调用函数(
    用传给reduce中的function（有两个参数）先对集合中的第1、2元素进行操作，得到的结果
    再与第三个数据进行function函数运算，最后得到一个结果)
'''
l = [1, 2, 3, 4, 5]
new_list = map(lambda x: x * 2, l)

print(new_list.__next__())
print(new_list.__next__())
print(new_list.__next__())
print(new_list.__next__())
print(new_list.__next__())


new_list1 = filter(lambda x: x % 2 == 0, l)

print(new_list1.__next__())
print(new_list1.__next__())


new_reduce = reduce(lambda x, y: x * y, l)

print(new_reduce)


'''
sorted函数是属于函数式编程，调用后会产生一个新的值，而不会改变原来的输入

所谓的函数式编程，是指代码中的每一块都是不可变的，都由纯函数的形式组成。这里的纯函数，是指函数本身
相互独立、互不影响，对于相同的输入，总会有相同的输出，没有任何副作用。

'''

d = {'mike': 10, 'lucy': 2, 'ben': 3}

s=dict(sorted(d.items(),key=lambda x:-x[1]))

print(s)
