import random


class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


def print_zb(zb):
    while zb is not None:
        if zb.val != None:
            print(zb.val)
        zb = zb.next


def has_more_ones(num):
    c = [0, 0, 0]
    while num > 0:
        c[num % 3] += 1
        num //= 3
    return c[1] > c[2]


def rmv_if_more_ones(head):
    if head.next is None:
        return
    rmv_if_more_ones(head.next)
    if head.next is not None and has_more_ones(head.next.val):
        head.next = head.next.next


s = Node()
zb = s
l = [1,3,3,2,2,2,1,1,1]

for i in range(len(l)):
    zb.next = Node(l[i])
    zb = zb.next
print_zb(s)
print("---")
rmv_if_more_ones(s)
print_zb(s)
