# def quick_sort(arr):
#     def partition(arr,left,right):
#         pivot=arr[left]
#         while left<right:
#             while left<right and arr[right]>pivot:
#                 right-=1
#             if left<right:
#                 arr[left]=arr[right]
#             while left<right and arr[left]<pivot:
#                 left+=1
#             if left<right:
#                 arr[right]=arr[left]
#         arr[left]=pivot
#         return left
#
#     def inner_quick_sort(arr,left,right):
#         stack =[]
#         stack.append(left)
#         stack.append(right)
#         while len(stack) >0:
#             right=stack.pop()
#             left=stack.pop()
#             pivot_index=partition(arr,left,right)
#
#             if pivot_index+1<right:
#                 stack.append(pivot_index+1)
#                 stack.append(right)
#             if pivot_index>left+1:
#                 stack.append(left)
#                 stack.append(pivot_index-1)
#     inner_quick_sort(arr,0,len(arr)-1)
#
#
# arr=[394,129,11,39,28]
# quick_sort(arr)
# print(arr)

'''
闭包：本质是一个函数，包裹着外部函数的变量（一般来说，函数中局部变量仅在函数执行期间可用），
变量的可见范围随同包裹，哪里可以访问到这个包裹，哪里就可以访问到这个变量
所有函数都有一个_closure_属性，如果这个函数是一个闭包的话，那么它返回的是一个由cell对象组成的元组对象，
cell对象的cell_centents属性就是闭包中的自由变量
'''