"""
Zadanie 8. Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
"""
from random import randint


def f(n):
    t = [randint(1, n) for _ in range(n)]
    print(t)
    succT = [False for _ in range(n)]
    succT[n-1] = True
    i = n - 3
    while i >= 0:
        l = t[i]
        d = 2
        while l > 1:
            if l % d == 0:
                if i+d < n and succT[i+d]:
                    succT[i] = True
                    break
                l //= d
            else:
                d += 1
        i -= 1
    return succT[0]


print(f(20))
