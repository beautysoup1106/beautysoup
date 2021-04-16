
from quick_sort_old import quick_sort_old

import time

'''
快排优化：
    1、单边递归优化：当本层完成了partition操作后，让本层继续完成基准左边的partition操作，而基准值右边的排序工作，
        交给下一层递归函数去处理。通过减少函数的调用次数，提高程序运行效率
    2、基准值选取优化：三点取中（取头，尾，中间，选择值大小中间的值），增加基准值选取的合理性
    3、partiti操作优化：头指针向后查找大于基准值的元素，尾指针向前查找小于基准值的元素，找到后，交换头尾指针所指向的元素，重复
        直到头尾指针交错后结束。
'''




def select_value(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return b


def quick_sort_new(arr, l, r):
    while l < r:
        x = l
        y = r
        z = select_value(arr[l], arr[r], arr[(l + r) >> 1])
        while True:
            while (arr[x] < z):
                x += 1
            while (arr[y] > z):
                y -= 1
            if (x <= y):
                arr[x], arr[y] = arr[y], arr[x]
                x += 1
                y -= 1
                break
        quick_sort_new(arr, x, r)
        r = y
    return

b=[7,4,9,1,3,10,5,6,8,2]
l=0
r=len(b)-1
# start_time1=time.perf_counter()
quick_sort_new(b,l,r)
# end_time1=time.perf_counter()
# print('old method cost :{}'.format(end_time1-start_time1))

# start_time2=time.perf_counter()
# quick_sort_old(l,r,b)
# end_time2=time.perf_counter()

# print('new method cost:{}'.format(end_time2-start_time2))

print(b)


