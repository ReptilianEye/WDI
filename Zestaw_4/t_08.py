"""
Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
się znaleźć taki ciąg oraz długość tego ciągu.
"""
import random
n = 5
T = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]


def printT(T):
    for t in T:
        for el in t:
            print(el, end=" ")
        print()
    print()


printT(T)


def check_length(i, j, q):
    n = len(T)
    length = 3
    while i+1 < n and j+1 < n and T[i+1][j+1] / T[i][j] == q:
        length += 1
        i += 1
        j += 1
    return length


def f(T):
    n = len(T)
    max_l = -1
    for i in range(n-2):
        for j in range(n-2):
            if len(set((T[i+1][j+1] / T[i][j], T[i+2][j+2] / T[i+1][j+1]))) == 1:
                l = check_length(i+2, j+2, T[i+1][j+1] / T[i][j])
                max_l = max(max_l, l)
    if max_l == -1:
        print("Nie ma")
    else:
        print(max_l)


f(T)
