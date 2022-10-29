"""
Zadanie 16. Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
jeden element największy(liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej wartości).
"""
from random import randint
t = []


def sol_easy(n):
    # t = [randint(1, 1000_000) for _ in range(n)]
    return t.count(max(t)) == 1 and t.count(min(t)) == 1


def f(n):
    # t = [randint(1,1000_000) for _ in range(n)]
    # t = [1, 2, 2, 3, 6, 7, 9]
    max_n = -1
    did_max_repeat = False
    min_n = 1e10
    did_min_repeat = False
    for el in t:
        if el == max_n:
            did_max_repeat = True
        if el == min_n:
            did_min_repeat = True
        if max_n < el:
            max_n = el
            did_max_repeat = False
        if min_n > el:
            min_n = el
            did_min_repeat = False
    return (not did_max_repeat and not did_min_repeat)

# for i in range(100):
#     t = [randint(1, 1000_000) for _ in range(100000)]
#     if sol_easy(i) != f(i):
#         print("Nie zgadza sie")
#         print(t)
#     print(i)
# print("skoczone")
