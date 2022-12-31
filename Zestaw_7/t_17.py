import random


class Node:
    def __init__(self, prev=None, val=None) -> None:
        self.val = val
        self.prev = prev
        self.next = None


def print_zb(zb):
    while zb is not None:
        if zb.val != None:
            print(zb.val)
        zb = zb.next


def odd_ones(num):
    c = 0
    while num > 0:
        c += num % 2
        num //= 2
    return c % 2 == 1


def rmv_if(head):
    zb = head.next
    prev = head
    while zb is not None:
        if odd_ones(zb.val):
            prev.next = zb.next
            zb.next.prev = prev
        prev = zb
        zb = zb.next


s = Node()
zb = s
l = [1, 2, 3, 4, 5]
prev = s
for i in range(5):
    zb.next = Node(prev, l[i])
    # zb.next = Node(s,random.randint(1, 100))
    prev = zb
    zb = zb.next
print_zb(s)
print("---")
rmv_if(s)
print_zb(s)
