"""
Zadanie 17. Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w obu
tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element (z
tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.
"""


def is_prime(n):
    if n < 2:  # wywalenie 0 i 1
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6
    while (i-1)**2 <= n:
        if n % (i-1) == 0 or n % (i+1) == 0:
            return False
        i += 6
    return True


# w tej wersji programu zakladam ze tablice sa tak samo dlugie
c = 0


def f(t1, t2, n, s, i):
    global c
    if i == n:
        # print(s)
        if is_prime(s):
            c += 1
            print(s, end=", ")
        return
    f(t1, t2, n, s+t1[i], i+1)
    f(t1, t2, n, s+t2[i], i+1)
    f(t1, t2, n, s+t1[i]+t2[i], i+1)


t1 = [3, 6, 20]
t2 = [45, 7, 11]
print("Prawidłowe sumy: ")
f(t1, t2, 3, 0, 0)
print()
print("Prawidłowych sum jest:", c)
