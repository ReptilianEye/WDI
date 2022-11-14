"""
Zadanie 9. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
"""

T = [[1, 2, 3, 4, 4], [1, 2, 3, 7, 10], [1, 2, 3, 5, 2], [1, 2, 7, 1, 2]]


def printT(T):
    for t in T:
        for el in t:
            print(el, end=" ")
        print()
    print()


printT(T)


def f(T, k):
    n = len(T)
    s_i = 0
    while s_i + 2 < n:
        s_j = 0
        while s_j + 2 < n:
            i = 2
            while s_i + i < n:
                j = 2
                while s_j + j < n:
                    if T[s_i][s_j] * T[s_i][s_j+j] * T[s_i+i][s_j] * T[s_i+i][s_j+j] == k:
                        return (i//2 + s_i, j//2+s_j)
                    j += 2
                i += 2
            s_j += 1
        s_i += 1
    return "Nie ma takiego"


print(f(T, 11))
