"""
Zadanie 1. Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
naturalnymi po spirali.
"""


def printT():
    for t in T:
        for el in t:
            print(el, end=" ")
        print()
    print()


def fill_line(i, j, i_k, j_k, l):
    while i != i_k or j != j_k:
        T[i][j] = l
        l += 1
        if i_k - i > 0:
            i += 1
        elif i_k - i < 0:
            i -= 1
        if j_k - j > 0:
            j += 1
        elif j_k - j < 0:
            j -= 1
    T[i][j] = l
    return l


def fill_circle(T):
    k = len(T)
    p = 0
    l = 1
    i = 0
    j = 0
    while l != len(T)*len(T):
        # T[i][j] = l
        # l += 1
        if i == p and j == p:
            l = fill_line(i, j, i, k-1, l)
            j = k-1
        elif i == p and j == k-1:
            l = fill_line(i, j, k-1, j, l)
            i = k - 1
        elif i == k-1 and j == k-1:
            l = fill_line(i, j, i, p, l)
            j = p
        elif i == k-1 and j == p:
            l = fill_line(i, j, p+1, j, l)
            p += 1
            k -= 1
            i = j = p
            l += 1
    T[i][j] = l
    printT()


n = 6
T = [[0 for _ in range(n)] for _ in range(n)]
fill_circle(T)

# fill_circle(T)
