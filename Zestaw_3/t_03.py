"""
Zadanie 3. Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.
"""


def f(n):
    n += 1
    primes = [True for _ in range(n)]
    primes[0] = primes[1] = False
    i = 2
    while i*i < n:
        if primes[i]:
            j = i+i
            while j < n:
                primes[j] = False
                j += i
        i += 1
    for i in range(n):
        if primes[i]:
            print(i, end=" ")


f(100)
