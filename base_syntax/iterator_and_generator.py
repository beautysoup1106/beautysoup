'''
判断一个对象是否可迭代
迭代器是一个有限集合
'''
import os
import time

import psutil as psutil


def is_iterator(params):
    try:
        iter(params)
        return True
    except TypeError:
        return False


params = [
    123,
    '1234',
    [1, 2, 3, 4, 5],
    set([1, 2, 3, 4]),
    {1: 1, 2: 2, 3: 3, 4: 4},
    (1, 2, 3, 4)
]
for i in params:
    print('{} is iterator? {}'.format(i, is_iterator(i)))

'''
生成器：可以成为一个无限集
'''


def show_mem_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memery used:{} MB'.format(hint, memory))


def test_iterator():
    show_mem_info('init iterator')
    list_1 = [i for i in range(1000000)]
    show_mem_info('after iterator')
    print(sum(list_1))
    show_mem_info('sum called')


def test_generator():
    show_mem_info('init generator')
    list_2 = (i for i in range(1000000))
    show_mem_info('after generator')
    print(sum(list_2))
    show_mem_info('sum called')


test_iterator()
test_generator()

'''
函数生成器
'''


def generator(k):
    i = 1
    while True:
        yield i ** i
        '''
        yield魔法：程序运行至这一行，会暂停，然后跳出。当next被调用的时候，暂停的程序又复活了，
        从yield这里将继续向下执行，同时变量i并没有被清除掉，而是会继续累加。
        速度不是yield的意义，空间才是
        '''
        i += 1


gen_1 = generator(1)
gen_3 = generator(3)


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1={},next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)


get_sum(8)

'''
生成器用法---返回指定数字下标
'''


def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i


print(list(index_generator([3, 2, 3, 4, 3, 7, 3], 3)))

'''
生成器用法---查找序列1是不是序列2的子序列
'''


def is_subsequence(a, b):
    b = iter(b)
    print(b)

    gen = (i for i in a)

    for i in gen:
        print(i)

    # print(next(gen))

    gen = ((i in b) for i in a)
    print(gen)

    for i in gen:
        print(i)

    print('----------------------------')

    return all(((i in b) for i in a))

#迭代器b已经消耗完毕,所以返回False，而A是列表，可迭代对象，所以没有消耗
print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
