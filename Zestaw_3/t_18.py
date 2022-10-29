"""
Zadanie 18. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
"""
import random
# t = [random.randint(1, 100) for _ in range(n)]


def is_palindrome_odd(s, e):
    while s < e:
        if t[s] != t[e]:
            return False
        if t[s] % 2 == 0:
            return False
        s += 1
        e -= 1
    return t[s] % 2 == 1  # zabezpiecza przypadek jednoelementowego podciagu


# t = [1, 2, 2, 5, 3, 3, 5, 3, 3, 2, 5]
t = [2, 4, 8]
n = len(t)


def f(n):
    # t = (random.randint(1, 1000) for _ in range(n))
    s = 0
    max_l = 0
    while s - 1 < n:
        e = s
        while e < n:
            if max_l < e-s+1:
                if is_palindrome_odd(s, e):
                    max_l = max(max_l, e-s+1)
                    print((s, e))
            e += 1
        s += 1
    print(max_l)


f(len(t))
