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


def add_nums(n1, n2):
    start = Node()
    new = start
    n1 = n1.next
    n2 = n2.next
    r = 0
    while n1 and n2:
        newV = n1.val + n2.val + r
        r = newV // 10
        new.next = Node(newV % 10)
        n1 = n1.next
        n2 = n2.next
        new = new.next
    while n1:
        newV = n1.val + r
        r = newV // 10
        new.next = Node(newV % 10)
        if r == 0:
            new.next.next = n1.next
            return start
        new.next = n1
    while n2:
        newV = n2.val + r
        r = newV // 10
        new.next = Node(newV % 10)
        if r == 0:
            new.next.next = n2.next
            return start
        new.next = n2
    if r > 0:
        new.next = Node(r)
    return start


start1 = Node()
zb = start1
for i in range(3):
    zb.next = Node(random.randint(1, 9))
    zb = zb.next
print_zb(start1)
print("---")
start2 = Node()
zb = start2
for i in range(5):
    zb.next = Node(random.randint(1, 9))
    zb = zb.next
print_zb(start2)
print("---")
new = add_nums(start1, start2)
print_zb(new)
