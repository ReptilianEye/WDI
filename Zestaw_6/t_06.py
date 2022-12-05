"""
Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elemen-
tów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.
"""


def lowestSum(T, s=0, s_index=0, i=0):
    if i == len(T):
        if s == s_index:
            print(s)
            exit()
        return
    # sumy.append(T[i])
    # indexy.append(i)
    lowestSum(T, s+T[i], s_index+i, i+1)
    lowestSum(T, s, s_index, i+1)
    # sumy.pop()
    # indexy.pop()


t = [1, 7, 3, 5, 11, 2]
lowestSum(t)
