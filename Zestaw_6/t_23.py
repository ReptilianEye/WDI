"""
Zadanie 23. Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory
"""
# w szczegolnosci rezystory mozna polaczyć szeregowo i rownolegle na wszystkie kombinacje
import numpy


def rezystory(T, R, max=3):
    def sprawdz_polaczenia(R, taken):
        if R == sum(taken):
            return True
        if R == numpy.prod(taken)/sum(taken):
            return True
        for i in range(len(taken)):
            if R == (numpy.prod(taken)/taken[i]) / (numpy.sum(taken)-taken[i]) + taken[i]:
                return True
        return False

    def rez_r(T, R, max, taken, i=0,  cnt=0):
        if cnt == max:
            # return sprawdz_polaczenia(R, taken)
            if sprawdz_polaczenia(R, taken):
                print(taken)
                return True
            else:
                return False
        if i >= len(T):
            return False
        if not rez_r(T, R, max, taken, i+1, cnt):
            taken[cnt] = T[i]
            return rez_r(T, R, max, taken, i+1, cnt+1)
        else:
            return True
    taken = [0 for _ in range(max)]
    return rez_r(T, R, max, taken)


T = [3, 12, 5, 6, 9]
print(rezystory(T, 13, 3))
