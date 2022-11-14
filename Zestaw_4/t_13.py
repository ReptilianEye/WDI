"""
Zadanie 13. Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica
T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie posiadające
liczby komplementarnej.
"""
T = [[4, 4, 3], [5, 5, 5], [5, 7, 5]]


def printT(T):
    for t in T:
        for el in t:
            print(el, end=" ")
        print()
    print()


printT(T)


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


def find_comp(l, n):
    for i in range(n):
        for j in range(n):
            if T[i][j] != 0 and is_prime(T[i][j]+l):
                return True
    return False


def f(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if not find_comp(T[i][j],n):
                T[i][j] = 0
    printT(T)
f(T)