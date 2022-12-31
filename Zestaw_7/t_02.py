class Node:
    def __init__(self, val, index) -> None:
        self.val = val
        self.index = index
        self.next = None


class rare_arr:
    def __init__(self, n, default=0) -> None:
        self.n = n
        self.first = None
        self.default = default

    def read(self, i):
        if i >= self.n:
            return None
        else:
            zb = self.first
            prev = zb
            while zb is not None and zb.index < i:
                prev = zb
                zb = zb.next
            if zb is not None and prev.index == i:
                return prev.val
            return self.default

    def update(self, i, val):
        if i < self.n:
            zb = self.first
            prev = zb
            while zb is not None and zb.index < i:
                prev = zb
                zb = zb.next
            if zb is not None and prev.index == i:
                prev.val = val
            else:
                el = Node(val, i)
                prev.next = el
                el.next = zb
