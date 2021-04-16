# def heapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#
#     if l<n and arr[i]<arr[l]:
#         largest=l
#
#     if r<n and arr[largest]<arr[r]:
#         largest=r
#
#     if largest!=i:
#         arr[i],arr[largest]=arr[largest],arr[i]
#
#         heapify(arr,n,largest)
#
# def heapSort(arr):
#     n=len(arr)
#
#     for i in range(n,-1,-1):
#         heapify(arr,n,i)
#
#     for i in range(n-1,0,-1):
#
#         arr[i],arr[0]=arr[0],arr[i]
#
#         heapify(arr,i,0)
#
# arr=[12,11,13,5,8,1]
#
# heapSort(arr)
#
# print(arr)
import cProfile
import math
import sys


# def heap(list):
#     n=len(list)
#     for i in range(0,int(math.log(n,2))):
#         for j in range(0,n//2):
#             k=2*j+2 if 2*j+2 <n and list[2*j+2]<list[2*j+1] else 2*j+1
#             if list[j]>list[k]:
#                 list[j],list[k]=list[k],list[j]
#
# if __name__ == '__main__':
#     list=[1,8,2,23,7,-4,18,23,42,37,2]
#     heap(list)
#     print(list)

def sink(list, root):
    if 2 * root + 1 < len(list):
        k = 2 * root + 2 if 2 * root + 2 < len(list) and list[2 * root + 2] < list[2 * root + 1] else 2 * root + 1
        if list[root] > list[k]:
            list[root], list[k] = list[k], list[root]
            sink(list, k)

if __name__ == '__main__':
    list = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    for i in range(len(list) // 2 - 1, -1, -1):
        cProfile.run('sink(list, i)')
    print(list)
