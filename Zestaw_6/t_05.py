"""
Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
110100 nie jest możliwe.
"""


from math import log10, floor


def primes_sito(n):
    n = (n+2)**2
    primes = [True for _ in range(n)]
    primes[0] = primes[1] = False
    i = 2
    while i*i <= n:
        if primes[i]:
            j = i*i
            while j < n:
                primes[j] = False
                j += i
        i += 1
    return primes


def get_from_bin(t):
    num = 0
    i = 0
    n = len(t)
    while i < n:
        num += 2**i*t[n-i-1]
        i += 1

    return num

def znajdzPierwszePodciagi(T):
    primes = primes_sito(len(T))

    success = False

    def pierwsze_podciagi_r(T, start=0):
        nonlocal success
        print(T[start:])
        if start == len(T)-1:
            success = True
        for i in range(len(T)):
            if primes(get_from_bin(T[start:i])):
                pierwsze_podciagi_r(T,i)

T = [1,1,1,0,1]
znajdzPierwszePodciagi(T)
