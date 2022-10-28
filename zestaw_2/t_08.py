"""
Zadanie 8. Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego, np. 9, 14, 15, 17, 22.
Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i wypisuje następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.
"""


def find_if_sum_of_fib(n):
    a = 1
    b = 1
    sum = 0
    while sum < n:
        sum = sum + a
        b = a+b
        a = b - a
    a = 1
    b = 1
    while sum > n:
        sum -= a
        b = b + a
        a = b - a

    if sum == n:
        return True
    else:
        return False
# sprawdzamy kolejno liczbe od n+1 az do momentu kiedy znajdziemy liczbe ktorej sie nie da przestawic jako spojny ciag
# (room for impovement)


def f(n):
    n = n + 1
    while find_if_sum_of_fib(n):
        n += 1
    else:
        print(n)
