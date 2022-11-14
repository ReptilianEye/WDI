"""
Zadanie 18. Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
maksymalnego podciągu.
"""
import random
n = 5
T = [[random.randint(1, 30) for _ in range(n)] for _ in range(n)]


def printT():
    for t in T:
        for el in t:
            print(el, end=" ")
        print()
    print()


printT()


def sum_podciagu(i, j, poz):
    inc = 0
    s = 0
    while inc < 10:
        if poz:
            if j + inc == n:
                return s
            s += T[i][j+inc]
        else:
            if i + inc == n:
                return s
            s += T[i+inc][j]
        inc += 1
    return s


def f(T):
    s_max = -1
    n = len(T)
    for i in range(n):
        for j in range(n):
            s_max = max(s_max, sum_podciagu(i, j, True))
            s_max = max(s_max, sum_podciagu(i, j, False))
    print(s_max)


f(T)
