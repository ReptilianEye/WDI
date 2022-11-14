import random
"""
Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
parzystą.

"""


def has_at_least_d_even(n): #sprawdza czy liczba ma co najmniej jedna cyfre parzysta
    while n > 0:
        if n % 2 == 0:
            return True
        n //= 10
    return False


def has_num_e_d_only(t):
    for el in t:
        if not has_at_least_d_even(el):
            return False
    return True


def f(T):
    for t in T:
        if has_num_e_d_only(t):
            print(t)
            return True
    return False


n = 5
T = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
print(T)
print(f(T))
