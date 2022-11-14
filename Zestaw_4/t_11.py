"""
Zadanie 11. Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
przyjaciółkami
"""
import random
n = 5
T = [[random.randint(1,20) for _ in range(n)] for _ in range(n)]

def printT(T):
    for t in T:
        for el in t:
            print(el, end=" ")
        print()
    print()
printT(T)
def get__bitmask_of_digits(n):
    digits = [False for _ in range(10)]
    while n != 0:
        digits[n % 10] = True
        n //= 10
    mask = ""
    for el in digits:
        if el:
            mask = mask+"1"
        else:
            mask = mask+"0"
    return mask


def f(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            T[i][j] = get__bitmask_of_digits(T[i][j])
    c = 0
    for i in range(n):
        for j in range(n):
            me = T[i][j]
            if (i == 0 or me == T[i-1][j]) and (j == 0 or me == T[i][j-1]) and (i == n-1 or me == T[i+1][j]) and (j == n-1 or T[i][j+1]):
                c += 1
    print(c) 
    return c
f(T)