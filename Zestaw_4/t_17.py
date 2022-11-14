"""
Zadanie 17. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa.
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

def sum_around(T, i, j):
    n = len(T)
    s = 0
    if i-1 >= 0:
        s += T[i-1][j]
    if j-1 >= 0:
        s += T[i][j-1]
    if i + 1 < n:
        s += T[i+1][j]
    if j + 1 < n:
        s += T[i][j+1]
    return s


def f(T):
    n = len(T)
    row = -1
    col = -1
    s_max = -1
    for i in range(n):
        for j in range(n):
            s = sum_around(T, i, j)
            if s_max < s:
                s_max = s
                row = i
                col = j
    print(col,row)


f(T)
