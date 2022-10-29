"""
Zadanie 11. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość najdłuższego,
 spójnego podciągu geometrycznego.
"""
from random import randint
n = 20
t = [randint(1, n) for _ in range(n)]
# t = [1,2,4,6,12,24,48]
# n = len(t)
print(t)


def f(n):
    if n == 1:
        print(1)
        return
    d_max = -1
    # r_max = -1
    d = 2
    q = t[1]/t[0]
    i = 2
    while i < n:
        if t[i] / t[i-1] == q:
            d += 1
        else:
            # if d_max < d:
            #     d_max = d
            #     r_max = r
            d_max = max(d_max, d)
            d = 2
            q = t[i] / t[i-1]
        i += 1
    # if d_max < d:
    #     d_max = d
    #     r_max = r
    d_max = max(d_max, d)
    # print(d_max,r_max)
    print(d_max)


f(n)
