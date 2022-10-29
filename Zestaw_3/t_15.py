"""
Zadanie 15. Dana jest duża tablica t. Proszę napisać funkcję, która zwraca informację czy w tablicy
zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”
"""


from random import randint


def erat_sieve(n):
    n += 1
    sieve = [True for _ in range(n)]
    sieve[0] = False
    sieve[1] = False
    i = 2
    while i*i < n:
        if sieve[i]:
            j = i*i
            while j < n:
                sieve[j] = False
                j += i
        i += 1
    return sieve


required = """wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą"""


def f(n):
    t = [randint(1, 1000_000) for _ in range(n)]
    sieve = erat_sieve(max(t))
    a = 1
    b = 1
    while a < n:
        if sieve[t[a]]:
            print(f"liczba {t[a]}, jest liczbą pierwsza, stoi na pozycji {a}")
            return False
        b = a + b
        a = b - a
    for i in range(n):
        if sieve[t[i]]:
            print(required)
            return True
    print("Warunek nie spełniony - nie ma prynajmniej jednej liczby 1")


f(1000)
