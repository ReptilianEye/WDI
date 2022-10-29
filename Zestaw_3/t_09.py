"""
Zadanie 9. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
długość najdłuższego, spójnego podciągu rosnącego.
"""
from random import randint
n = 20
t = [randint(1, n) for _ in range(n)]
print(t)


def f(n):
    d_max = -1
    d = 1
    i = 1
    while i < n:
        if t[i] > t[i-1]:
            d += 1
        else:
            d_max = max(d_max, d)
            d = 1
        i += 1
    d_max = max(d_max, d)
    print(d_max)


f(n)
