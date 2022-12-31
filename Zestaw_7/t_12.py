import random


class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


def insert(head, s):
    if head.next is None:
        head.next = Node(s)
        return True
    zb = head.next
    prev = head
    while zb is not None and zb.val < s:
        prev = zb
        zb = zb.next
    if zb is None or zb.val > s:
        s = Node(s)
        if zb == head.next:
            s.next = head.next
            head.next = s
            return True
        else:
            prev.next = s
            s.next = zb
            return True
    return False


def print_zb(zb):
    while zb is not None:
        if zb.val != None:
            print(zb.val)
        zb = zb.next


a = "aac"
b = "abc"
c = "xyz"
l = [a, b, c]
s = Node()
zb = s
for i in range(3):
    zb.next = Node(l[i])
    zb = zb.next
print_zb(s)
print("---")
if insert(s, "zzz"):
    print("dodane")
print_zb(s)
