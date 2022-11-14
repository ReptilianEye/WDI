"""
Zadanie 14. Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2>N1. Proszę napisać funkcję,
która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne tablice powinny
pozostać nie zmieniane.
"""


def num_of_1(n):
    l = 0
    while n > 0:
        if n % 2 == 1:
            l += 1
        n //= 2
    return l


def change_t(tt):
    for i in range(len(tt)):
        for j in range(len(tt)):
            tt[i][j] = num_of_1(tt[i][j])


def check_match(T1, T2, x, y):
    n = len(T1)
    c = 0
    for i in range(n):
        for j in range(n):
            if T1[i][j] == T2[i+x][j+y]:
                c += 1
    return c


# # t2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# # t1 = [[2, 3], [2, 3]]
# print(check_match(t1,t2,0,1))

def f(T1, T2):
    T1 = change_t(T1)
    T2 = change_t(T2)
    n1 = len(T1)
    n2 = len(T2)
    for i in range(n2-n1):
        for j in range(n2-n1):
            matched = check_match(T1, T2, i, j)
            if matched/(n1*n1)*100 > 33:
                return True
