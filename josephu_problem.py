class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def createLink(n):
    if n <= 0:
        return False
    if n == 1:
        return None
    else:
        root = Node(1)
        tmp = root
        for i in range(2, n + 1):
            tmp.next = Node(i)
            tmp = tmp.next
        tmp.next = root
        return root


def shwoLink(root):
    tmp = root
    while True:
        print(tmp.value)
        tmp = tmp.next
        if tmp == None or tmp == root:
            break


def josephu(n, k):
    if k == 1:
        print('survive:', n)
        return
    root = createLink(n)
    tmp = root
    while True:
        for i in range(k - 2):
            tmp = tmp.next
        print('kill', tmp.next.value)
        tmp.next = tmp.next.next
        tmp = tmp.next
        if tmp.next == tmp:
            break

    print('survive last:', tmp.value)


def josephu2(n, k):
    if k == 1:
        print('survive:', n)
        return
    p = 0
    people = list(range(1, n + 1))
    while True:
        if len(people) == 1:
            break
        p = (p + (k - 1)) % len(people)
        print('kill', people[p])
        del people[p]
    print('survive：', people[0])


def josephu3(n, k):
    if n == 1:
        return 1
    val = 0
    for i in range(2, n + 1):
        cul = (val + k) % i
        print(cul)
        val = cul
    return val + 1


if __name__ == '__main__':
    # josephu(5, 2)
    # print('---------------------')
    # josephu2(6, 5)
    # print('-----------------')
    s=josephu3(10, 4)
    print(s)