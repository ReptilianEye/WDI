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


def del_double(head):
    zb = head.next
    fast = zb
    while fast:
        for _ in range(2):
            fast = fast.next
            if fast is None:
                zb.next = None
                return
        zb.next = fast
        zb = zb.next


start = Node()
zb = start
for i in range(6):
    zb.next = Node(random.randint(1, 50))
    zb = zb.next
print_zb(start)
print("---")
del_double(start)
print_zb(start)
