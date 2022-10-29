"""
Zadanie 7. Napisać program wypełniający N-elementową tablicę t liczbami pseudolosowymi z zakresu
1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
"""
from random import randint


def f(n):
    t = [randint(1, 1000) for _ in range(n)]
    print(t)
    for el in t:
        el2 = el
        while el2 > 0:
            if el2 % 10 == 2:
                break
            el2 //= 10
        else:
            print(el)
            break


f(100)
