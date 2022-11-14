"""
Zadanie 7. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
T2 były uporządkowane niemalejąco.
"""

import random


def printT(T):
    for t in T:
        for el in t:
            print(el, end=" ")
        print()
    print()


def find_next_lowest(T, prev_lowest):
    n = len(T)
    lowest = 10e10
    i_l = -1
    j_l = -1
    for i in range(n):
        for j in range(n):
            if T[i][j] > lowest:
                break
            if T[i][j] < lowest and T[i][j] >= prev_lowest:
                lowest = T[i][j]
                i_l = i
                j_l = j
    if lowest != 10e10:
        T[i_l][j_l] = lowest-1
    return lowest


n = 5
T1 = []
for i in range(n):
    t = [random.randint(0, 10)]
    for j in range(n-1):
        t.append(t[j] + random.randint(0, 10))
    T1.append(t)
T2 = [0 for _ in range(n*n)]

printT(T1)


def f(T1):
    printT(T1)
    i = 0
    lowest = find_next_lowest(T1, 0)
    while lowest != 10e10:
        T2[i] = lowest
        lowest = find_next_lowest(T1, lowest)
        i += 1
    print(T2)


f(T1)
