"""
Zadanie 12. Dana jest tablica T[N][N][N]. Proszę napisać funkcję, do której przekazujemy tablicę wypełnioną liczbami większymi od zera.
Funkcja powinna zwracać wartość True, jeżeli na wszystkich poziomach
tablicy liczba elementów sąsiadujących(w obrębia poziomu) z co najmniej 6 liczbami złożonymi jest jednakowa albo wartość False w przeciwnym przypadku.
"""


import random


def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6   # jesli sprawdzilismy czy liczba dzieli sie przez 2 i 3 to wystarczy sprawdzac kolejne liczby +1 -1 od 6, bo tylko to sa kandydaci na liczby 1
    while (i-1)**2 <= n+1:
        if n % (i-1) == 0 or n % (i+1) == 0:
            return False
        i += 6
    return True


n = 5
T = [[[random.randint(1, 30) for _ in range(n)]
      for _ in range(n)]for _ in range(n)]
# for tt in T:
#     for t in tt:
#         for el in t:
#             print(el, end=" ")
#         print()
#     print()


def printT(T):
    for t in T:
        for el in t:
            print(el, end=" ")
        print()
    print()


printT(T)


def count_n_to_nprime(tt):
    n = len(tt)
    marked = [[False for _ in range(n)] for _ in range(n)]
    c = 0
    for i in range(n):
        for j in range(n):
            if tt[i][j] not in [0, 1] and not is_prime(tt[i][j]):
                c += 1
                if i - 1 >= 0:
                    marked[i-1][j] = True
                if j - 1 >= 0:
                    marked[i][j-1] = True
                if i + 1 < n:
                    marked[i+1][j] = True
                if j + 1 < n:
                    marked[i][j+1] = True
                printT(marked)
    if c < 6:
        return -1
    s = 0
    for i in range(n):
        for j in range(n):
            if marked[i][j]:
                s += 1
    return s


def f(T):
    num_of_n = count_n_to_nprime(T[0])
    for i in range(1, len(T)):
        if num_of_n != count_n_to_nprime(T[i]):
            return False
    return True


count_n_to_nprime(T[0])
