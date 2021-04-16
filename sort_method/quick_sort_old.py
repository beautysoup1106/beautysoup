def quick_sort_old(l, r,arr):
    if (l >= r):
        return
    x = l
    y = r
    z = arr[l]
    while x < y:
        while (x < y and arr[y] >= z):
            y -= 1
        if (x < y):
            arr[x] = arr[y]
            x += 1
        while (x < y and arr[x] <= z):
            x += 1
        if (x < y):
            arr[y] = arr[x]
            y -= 1
    arr[x] = z
    quick_sort_old(l, x - 1,arr)
    quick_sort_old(x + 1, r,arr)
    return
if __name__ == '__main__':
    b=[7,4,9,1,3,10,5,6,8,2]
    l=0
    r=len(b)-1
    quick_sort_old(l,r,b)
    print(b)