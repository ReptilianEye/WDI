"""
Zadanie 6. Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
"""
from random import randint


def f(n):
    t = [randint(1, 1000) for _ in range(n)]
    print(t)
    for el in t:
        el2 = el
        while el2 > 0:
            if el2 % 2 == 1:
                break
            el2 //= 10
        else:
            print(el, "nie ma cyfry nieparzystej")
            break


f(100)
