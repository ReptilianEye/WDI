"""
Zadanie 16. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
będących liczbami pierwszymi?
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
        if if_one_prime_digits(el):
            return True
    return False


def f(T):
    for t in T:
        if not if_opd_in_t(t):
            return False
    return True

T = [[2,1,1],[2,2,2],[1,1,1]]
print(f(T))