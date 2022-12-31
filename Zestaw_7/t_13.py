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


def rmv_if_prev_lower(head):
    if head.next is None:
        return
    rmv_if_prev_lower(head.next)
    if head.val is not None:
        if head.next.val < head.val:
            head.next = head.next.next


s = Node()
zb = s
l = [20,10,7,3,100]
for i in range(len(l)):
    zb.next = Node(l[i])
    zb = zb.next
print_zb(s)
print("---")
rmv_if_prev_lower(s)
print_zb(s)


