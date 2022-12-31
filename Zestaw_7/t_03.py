class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def print_zb(zb):
    while zb is not None:
        if zb.val != None:
            print(zb.val)
        zb = zb.next


def merge(head1, head2):
    head1 = head1.next
    head2 = head2.next
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.val < head2.val:
        start = head1
        head1 = head1.next
    else:
        start = head2
        head2 = head2.next
    zb = start
    while head1 and head2:
        if head1.val < head2.val:
            zb.next = head1
            head1 = head1.next
        else:
            zb.next = head2
            head2 = head2.next
        zb = zb.next
    if head1:
        zb.next = head1
    if head2:
        zb.next = head2
    return start
    # start = start.next


first = Node(None)
first.next = Node(1)
first.next.next = Node(15)
first.next.next.next = Node(20)

first2 = Node(None)
first2.next = Node(4)
first2.next.next = Node(10)
first2.next.next.next = Node(11)

print_zb(first)
print("---")
print_zb(first2)
print("---")
new = merge(first, first2)
print_zb(new)
