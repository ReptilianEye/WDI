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

def rmv_if_div(head):
    zb = head.next
    prev = head
    while zb.next:
        if zb.next.val % zb.val == 0:
            prev.next = zb.next
        else:
            prev = zb
        zb = zb.next

s = Node()
zb = s
l = [20,1,2,4,16,17]
for i in range(len(l)):
    zb.next = Node(l[i])
    zb = zb.next
print_zb(s)
print("---")
rmv_if_div(s)
print_zb(s)
