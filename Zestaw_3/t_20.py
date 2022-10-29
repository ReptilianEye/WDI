"""
Zadanie 20. Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000.
Proszę napisać funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy, dla którego w iloczynie jego elementów każdy czynniki pierwszy występuje co najwyżej raz.
Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.
"""


import random


def has_unique_factors(n):
    i = 2
    if n < 2:
        return False
    while n > 1:
        if n % (i*i) == 0:
            return False
        elif n % i == 0:
            n //= i
        i += 1
        if i*i > n:
            break
    return True


def f(n):
    t = [random.randint(1, 1000) for _ in range(n)]

    # t = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22] #wynik 5
    # n = len(t)

    max_l = 0
    for i in range(n):
        multi = 1
        for j in range(i, n):
            multi *= t[j]
            if has_unique_factors(multi):
                max_l = max(max_l, j-i+1)
    print(max_l)


f(100)
