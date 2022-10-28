"""
Zadanie 12. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta zawiera cyfrę równą liczbie swoich cyfr.
"""
from math import log10, floor


def f(a):
    dig_count = floor(log10(a)) + 1
    while a != 0:
        if a % 10 == dig_count:
            return True
        a //= 10
    return False