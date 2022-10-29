"""
Zadanie 13. Proszę napisać program, który wypełnia N-elementową tablicę t trzycyfrowymi liczbami
pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w tablicy dla którego w tablicy występuje również rewers tego ciągu. Na przykład dla tablicy: t=
[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4
"""


from random import randint


def has_rewers(s, e):
    i = len(t) - 1
    while i >= 0:
        if t[i] == t[s]:
            j = 0
            while j <= e-s:
                if t[i-j] != t[s+j]:
                    break
                elif j == e-s:
                    return True
                j += 1
        i -= 1
    return False


n = 100
t = [randint(100, 999) for _ in range(n)]
# t = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15] #wynik 4


def f(t):
    n = len(t)
    i = 0
    max_l = 0
    while i < n:
        j = i
        while j < n:
            if has_rewers(i, j):
                max_l = max(max_l, j-i+1)
            j += 1
        i += 1
    print(max_l)


f(t)
