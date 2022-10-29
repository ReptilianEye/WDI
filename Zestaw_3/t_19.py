"""
Zadanie 19. Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
"""


import random


def sum_of_indexes(i, j):
    return int((i+j)/2*(abs(i-j)+1))


def f(n):
    t = [random.randint(1, 100) for _ in range(n)]
    max_l = 0
    i = 0
    while i < n:
        j = i
        s = 0
        while j < n:
            s += t[j]
            if s == sum_of_indexes(i, j):
                max_l = max(max_l, j-i+1)
                print(i, j)
            j += 1
        i += 1
    print(max_l)


f(100)
