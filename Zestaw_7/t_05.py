class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


def print_zb(zb):
    while zb is not None:
        if zb.val != None:
            print(zb.val)
        zb = zb.next


def split_l(head):
    if head.next is None:
        return head
    zb = head.next
    t_startow = [Node(None) for _ in range(10)]
    t_roboczych = [el for el in t_startow]
    while zb:
        poz = zb.val % 10
        t_roboczych[poz].next = zb
        t_roboczych[poz] = t_roboczych[poz].next
        zb = zb.next
    zb = head
    for i in range(10):
        t_roboczych[i].next = None
        t_startow[i] = t_startow[i].next
        while t_startow[i]:
            zb.next = t_startow[i]
            zb = zb.next
            t_startow[i] = t_startow[i].next

import random
start = Node()
zb = start
for i in range(20):
    zb.next = Node(random.randint(1,50))
    zb = zb.next
print_zb(start)
print("---")
split_l(start)
print_zb(start)
