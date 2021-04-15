'''
递归函数的两个要件：
    1、基线条件
        问题可以被分解为最小的问题，当满足基线条件时，递归就不再执行了
    2、递归条件
        有继续将问题分解的条件
    它的整体思想是，讲一个大问题分解为一个个的小问题，知道问题无法分解时，再去解决
    小问题，从而解决大问题
'''


# def merge_sort(arr, l, r):
#     if l == r:
#         return
#     mid = (l + r) >> 1
#     merge_sort(arr, l, mid)
#     merge_sort(arr, mid + 1, r)
#     merge(arr, l, mid, r)
#
#
# def merge(arr, l, mid, r):
#     temp = []
#     p1 = l
#     p2 = mid + 1
#     k = 0
#     while p1 <= mid or p2 <= r:
#         if p2>r or (p1<=mid and arr[p1]<arr[p2]):
#             temp.append(arr[p1])
#             k+=1
#             p1+=1
#         else:
#             temp.append(arr[p2])
#             k+=1
#             p2+=1
#
#     for i in range(r-l+1):
#         arr[l+i]=temp[i]
#
#     # return arr
#
#
# arr=[7,9,2,6,14,12]
# merge_sort(arr,0,len(arr)-1)
#
# print(arr)

def inversion_number(nums):
    def across_numbers(nums, left, mid, right):
        l, r = left, mid + 1
        temp = []
        inversion = 0
        while l <= mid or r <= right:
            if (r > right or l <= mid and nums[l] <= nums[r]):
                temp.append(nums[l])
                l += 1
            else:
                temp.append(nums[r])
                r += 1
                inversion += mid + 1 - l

        for i in range(right - left + 1):
            nums[left + i]=temp[i]
            # print('sort temp:',temp[i])
        # print(inversion)
        return inversion

    def merge_sort1(nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) >> 1
        # print('left begin-----')
        left_num = merge_sort1(nums, left, mid)
        # print('---------------right begin')
        right_num = merge_sort1(nums, mid + 1, right)

        # print('----sort begin-------')

        across_num = across_numbers(nums, left, mid, right)

        return left_num + right_num + across_num

    return merge_sort1(nums,0,len(nums)-1)


arr = [7, 9, 2, 6, 14, 12]
x = inversion_number(arr)

print(x)
# merge_sort(arr,0,len(arr)-1)
