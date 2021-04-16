import cProfile

'''
list.count(obj)：统计obj在list中出现的次数
list.extend(seq):在list末尾追加seq中的多个值
list.index(obj):从list中找出obj第一个匹配项的index
list.insert(index,obj)：将obj插入列表index处
list.remove(obj)：移除iist中obj的第一个匹配项
list.reverse():反转列表

'''


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n - 1))
    res.append(fib(n))
    return res


cProfile.run('fib_seq(30)')


def memorize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memorize
def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib_seq1(n):
    res = []
    if n > 0:
        res.extend(fib_seq1(n - 1))
    res.append(fib1(n))
    return res


cProfile.run('fib_seq1(30)')
