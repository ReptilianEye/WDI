"""
Zadanie 21. Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę
zaimplementować funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
(1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
(2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
Funkcja powinna zwrócić liczbę znalezionych trójek.
"""

import random
from math import gcd


def trojki(t):
    n = len(t)
    i = 0
    c = 0
    while i < n-2:
        j = i + 1
        while j <= i + 2 and j < n - 1:
            k = j + 1
            while k <= j + 2 and k < n:
                if gcd(t[i], gcd(t[j], t[k])) == 1:
                    c += 1
                    # print(t[i], t[j], t[k])
                k += 1
            j += 1
        i += 1
    print("Takich trójek jest", c)


t = [random.randint(1, 50) for i in range(20)]
print(t)
trojki(t)
