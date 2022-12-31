class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


def print_zb(zb):
    while zb is not None:
        if zb.val != None:
            print(zb.val)
        zb = zb.next


def push_back(head, el):
    zb = head.next
    prev = zb
    while zb:
        prev = zb
        zb = zb.next
    prev.next = Node(el)


def pop(head):
    zb = head.next
    prev = zb
    while zb.next:
        prev = zb
        zb = zb.next
    prev.next = None

import random
start = Node()
zb = start
for i in range(5):
    zb.next = Node(random.randint(1, 50))
    zb = zb.next
print_zb(start)
print("---")
pop(start)
print_zb(start)
push_back(start,100000000)
print("---")
print_zb(start)
