class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def member(zb, el):
    while zb is not None:
        if zb.val == el:
            return True
        zb = zb.next
    return False


def insert(zb, el):
    if zb is None:
        return Node(el)
    start = zb
    prev = zb
    while zb is not None and zb.val < el:
        prev = zb
        zb = zb.next
    if zb is None or zb.val > el:
        el = Node(el)
        if zb == start:
            el.next = zb
            return el
        else:
            prev.next = el
            el.next = zb

    return start


def remove(zb, val):
    start = zb
    prev = zb
    while zb is not None and zb.val < val:
        prev = zb
        zb = zb.next
    if zb is None:
        return start
    if zb.val == val:
        if zb == start:
            return zb.next
        prev.next = zb.next
    return start


def print_zb(zb):
    while zb is not None:
        print(zb.val)
        zb = zb.next
