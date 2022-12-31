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


def rmv_or_add(el, head):
    prev = head
    zb = head.next
    while zb:
        if zb.val == el:
            prev.next = zb.next
            return
        prev = zb
        zb = zb.next
    prev.next = Node(el)


s = Node()
zb = s
els = list(set(random.randint(1, 9) for _ in range(10)))
random.shuffle(els)
for el in els:
    zb.next = Node(el)
    zb = zb.next
print_zb(s)
to_look = els[-5]
print("to_look",to_look)
rmv_or_add(to_look,s)
print_zb(s)

