"""
zad 1
Dana jest tablica liczb naturalnych. Poszukujemy w niej takiego ciągu liczb, dla którego zaraz za nim jest taki sam ciąg liczb,
ale każda jest zwiększona tyle samo razy.
Np. 2,3,5,7 --> 6,9,15,21
Nalezy zwrocic krotke z startowym i koncowym indexem tego ciagu:
np dla ciągu
3,3,2,2,3,5,7,6,9,15,21,1,1 odpowiedzią jest 3, 7
"""


def sequence(T):
    n = len(T)
    for dl in range(n//2, 2, -1):
        for i in range(n-dl*2+1):
            j = 0
            while j+1 < dl:
                if T[i+dl+j] / T[i + j] != T[i + dl + j + 1]/T[i + j + 1]:
                    break
                j += 1
            if j+1 == dl:
                return i, i+dl


# T = [3, 3, 2, 2, 3, 5, 7, 6, 9, 15, 21, 1,1]
# T = [2, 3, 5, 7, 6, 9, 15, 21]

# print(sequence(T))

"""
zad 2
Dana jest tablica kwadratowa liczb naturalnych. Dany jest ciąg 1,2,2,3,4,6....(taki że każdy kolejny element jest sumą dwóch poprzednich -1)
Znajdz najdłuższy podciąg tego ciągu w tablicy ułożony w taki sposób, że każdy kolejny element ma wiersz i kolumne wieksza niz poprzedni
"""


def if_element_of_seq(el):
    a = 1
    b = 2
    while a < el:
        a, b = b, a+b-1

    return a == el


def extend_seq(i, j, T):
    # i,j są wspolrzenymi dotyczasowego ciagu 3 elementowego, wiec pierwsze co zrobimy to je zwiekszymy
    n = len(T)
    i += 1
    j += 1
    dl = 3
    while i + 2 < n and j + 2 < n and T[i][j] + T[i+1][j+1] - 1 == T[i+2][j+2]:
        dl += 1
        i += 1
        j += 1
    return dl


def seq(T):
    n = len(T)
    max_l = -1
    for i in range(n-2):
        for j in range(n-2):
            if if_element_of_seq(T[i][j]) and if_element_of_seq(T[i+1][j+1]) and if_element_of_seq(T[i+2][j+2]):
                if T[i][j]+T[i+1][j+1] - 1 == T[i+2][j+2]:
                    max_l = max(max_l, extend_seq(i, j, T))
    return max_l


T = [[1, 2, 3, 1], [1, 2, 3, 1], [1, 2, 2, 1], [1, 2, 2, 3]]
print(seq(T))
