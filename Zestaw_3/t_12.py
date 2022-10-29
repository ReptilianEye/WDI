"""
Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego
o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
indeksach.
"""
from random import randint, randrange


def f(n):
    # t = [randrange(1,99, 2) for _ in range(n)] #wersja Miłosza
    # generowanie nieparzystych liczb pseudolosowych
    t = [randint(0, 49)*2+1 for _ in range(n)]
    print(t)
    d_r_max = -1  # dlugość rosnącego najdłuższego
    d_r = 1

    d_m_max = -1  # dlugość malejącego najdłuższego
    d_m = 1

    r = -1
    i = 1
    while i < n:
        r_next = t[i] - t[i-1]
        if r_next > 0:
            if r == r_next:
                d_r += 1
            else:
                d_r_max = max(d_r_max, d_r)
                d_r = 2
        elif r_next < 0:
            if r == r_next:
                d_m += 1
            else:
                d_m_max = max(d_m_max, d_r)
                d_m = 2
        i += 1
        r = r_next
    d_r_max = max(d_r_max, d_r)
    d_m_max = max(d_m_max, d_m)

    print(f"Najdłuższy ciąg arytmetyczny malejący ma długość {d_m_max}")
    print(f"Najdłuższy ciąg arytmetyczny rosnacy ma długość {d_r_max}")


f(20)
