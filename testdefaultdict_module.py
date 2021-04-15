from collections import defaultdict

'''
小整数池：python提前建立好范围在[-5,256]的整数对象，且不会被垃圾回收。无论这个整数处于LEGB中的哪个位置，所有位于这个范围内的
        整数都使用的是同一个对象。目的是为了避免频繁申请和销毁小整数的内存空间，提高程序的运行效率
哈希表设计思想：
        indice下标，entry入口，用下标去找对应元素。维护一个数据量较小的接口，去访问一个数据量较大的接口
        同理：
            函数的本质是在堆heap中放置的对象，函数名的本质是放在栈stack中的地址，指向堆中放置的对象
模块化：
        from module_name import * 会把module中所有的函数的和类全拿过来，如果和其他函数名有冲突导入就会报错
        import module也会导入所有函数和类，但是调用必须是用module_name.func来进行调用，相当于外面包装了一层，能有效避免冲突。
'''
def non():
    return None
d=defaultdict(non)

d['a']

print(d)