from functools import cmp_to_key

'''
sort(*,key=None,reverse = False)
functools.cmp_to_key（func ）
sort函数式对列表进行排序
key主要是用来进行比较的元素，只有一个参数，具体的参数就是取自可迭代对象中，指定可迭代对象中的一个元素来进行排序，每次
    排序前调用
cmp_to_key方法返回一个充当代理键的特殊对象。将旧式的比较函数(自定义函数)转换为关键函数key,则使用关键函数的方法，如
sort,min,max,heapq.nlargest,heapq.nsmallest可以调用。
该函数返回1，则表示大于，0则表示相当，负数则表示小于。
'''

num=[3,30,34,5,9]
new_nums=sorted(num,key=cmp_to_key(lambda x,y:y-x))
new_nums1=sorted(num,key=cmp_to_key(lambda x,y:x-y))
print(new_nums1)
print(new_nums)

num2=map(str,num)
new_nums3=sorted(num2,key=cmp_to_key(lambda x,y:int(x+y)-int(y+x)))