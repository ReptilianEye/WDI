"""
Zadanie 2. Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001
"""


def f(a, b):
    appearances = [0 for _ in range(10)]
    while a > 0:
        appearances[a % 10] += 1
        a //= 10
    while b > 0:
        appearances[b % 10] -= 1
        b //= 10
    # end
    print((sum(appearances) == 0))


f(123, 3221)
