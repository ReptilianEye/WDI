"""
Zadanie 15. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
będącą liczbą pierwszą?
"""
prime_digits = [2, 3, 5, 7]
def if_one_prime_digits(n):
    while n > 0:
        if n % 10 in prime_digits:
            return True
        n //= 10
    return False


def if_opd_in_t(t):
    for el in t:
        if not if_one_prime_digits(el):
            return False
    return True


def f(T):
    for t in T:
        if if_opd_in_t(t):
            return True
    return False


T = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(f(T))