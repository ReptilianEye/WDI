"""
Zadanie 22. Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.
"""

def skoki(T):
    def gen_czynniki(max):
        max += 1
        primes = [True for _ in range(max)]
        primes[0] = primes[1] = False
        i = 2
        while i*i < max:
            if primes[i]:
                j = i*i
                while j < max:
                    primes[j] = False
                    j += i
            i += 1
        return primes

    def skoki_r(T, primes, i=0, il_skokow=0):
        nonlocal min_skokow
        if i == len(T)-1:
            min_skokow = min(min_skokow, il_skokow)
            return
        wsk = T[i]-1
        while wsk > 1:
            if primes[wsk] and T[i] % wsk == 0 and i+wsk <= len(T):
                skoki_r(T, primes, i+wsk, il_skokow+1)
            wsk -=1
    primes = gen_czynniki(100)
    min_skokow = 10**10
    skoki_r(T, primes)
    return min_skokow


T = [6 for _ in range(11)]
print(skoki(T))
