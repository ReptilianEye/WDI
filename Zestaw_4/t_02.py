import random
"""
Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
z nieparzystych cyfr.
"""


def has_odd_digits(n):
    while n > 0:
        if n % 2 == 0:
            return False
        n //= 10
    return True


def has_num_e_d_only(t):
    for el in t:
        if has_odd_digits(el):
            return True
    return False


def f(T):
    for t in T:
        if not has_num_e_d_only(t):
            print(t)
            return "False"
    return True


n = 5
T = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
print(T)
print(f(T))
