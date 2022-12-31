class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def f(dHead,Whead1,Whead2):
    p1 = Whead1
    p2 = Whead2
    i = dHead
    count = 0
    while i.next is not None:
        i = i.next
        if i.val % 2 == 0 and i.val > 0:
            p1.next=i
            p1 = p1.next
        elif i.val%2==1 and i.val < 0:
            p2.next = i
            p2 = p2.next
        else:
            count += 1
    p1.next = None
    p2.next = None
    return count
