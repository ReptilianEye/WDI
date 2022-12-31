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

# liczba jest jest przechowywana od najmniej waznej cyfry


def inc_num(head):
    zb = head.next
    r = 1
    prev = zb
    while zb:
        prev = zb
        if r:
            zb.val = (zb.val + r) % 10
            r = zb.val == 0

        else:
            return
        zb = zb.next
    prev.next = Node(1)


start = Node()
zb = start
for i in range(3):
    zb.next = Node(random.randint(9, 9))
    zb = zb.next
print_zb(start)
print("---")
inc_num(start)
print_zb(start)
