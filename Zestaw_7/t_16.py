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


def even_fives(num):
    c = 0
    while num > 0:
        if num % 8 == 5:
            c += 1
        num //= 8
    return c % 2 == 0


def move_to_frond(head):
    zb = head.next
    prev = head
    while zb is not None:
        if even_fives(zb.val) and prev != head:
            prev.next = zb.next
            zb.next = head.next
            head.next = zb
            zb = prev.next
        else:    
            prev = zb
            zb = zb.next


s = Node()
zb = s
l = [1,2,3,4,5]
for i in range(5):
    # zb.next = Node(l[i])
    zb.next = Node(random.randint(1,100))
    
    zb = zb.next
print_zb(s)
print("---")
move_to_frond(s)
print_zb(s)
