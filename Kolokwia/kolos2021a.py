# napisane na kartce, to jest tylko spradzenie
"""
Zadanie 1 (5 pkt)
„Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych cyfr, gdzie
M, N ⩾ 0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
pierwszą o różnych cyfrach jaką można uzyskać z obcięcia liczby K albo 0, gdy taka liczba nie
istnieje. Na przykład dla liczby 1202742516 spośród obciętych liczb pierwszych: 2, 5, 7, 251, 2027
liczbą spełniającą warunek jest liczba 251.
"""


from math import log10


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6
    while i*i <= n:
        if n % (i-1) == 0 or n % (i+1) == 0:
            return False
        i += 6
    return True


def obroc_l(l):
    l_o = 0
    while l > 0:
        l_o = l_o * 10 + l % 10
        l //= 10
    return l_o


def obetnij(l, p, n):
    n = n // (10**p)
    n = obroc_l(n)
    n = n // (10**l)
    n = obroc_l(n)
    return n


def rozne_cyfry(n):
    cyfr = [False for _ in range(10)]
    while n > 0:
        cyfra = n % 10
        if cyfr[cyfra]:
            return False
        else:
            cyfr[cyfra] = True
        n //= 10
    return True

from math import floor
def f(n):
    max_prime = 0
    len_n = floor(log10(n))+1
    for l in range(len_n):
        for p in range(len_n):
            l_obc = obetnij(l, p, n)
            if is_prime(l_obc):
                # print(l_obc)
                if rozne_cyfry(l_obc):
                    max_prime = max(max_prime,l_obc)
    return max_prime

print(f(1202742516))