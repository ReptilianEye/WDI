"""
Zadanie 31. Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczy-
nów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć,
że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać po-
dzielniki do tablicy pomocniczej. Przykład: 60 →[2, 3, 5] →2 + 3 + 5 + 2 ∗3 + 2 ∗5 + 3 ∗5 + 2 ∗3 ∗5 = 71
"""

from math import sqrt
def rozklad(n):
    d = set()
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            d.add(i)
            n //= i
            i == 1
        i += 1
    return list(d)


def sum_of_podzbiorow(zb, i, il):
    # if i == len(zb):
    #     return il
    # return sum_of_podzbiorow(zb,i+1,il) + sum_of_podzbiorow(zb,i+1,il*zb[i])
    return il if i == len(zb) else sum_of_podzbiorow(zb, i+1, il) + sum_of_podzbiorow(zb, i+1, il*zb[i])
