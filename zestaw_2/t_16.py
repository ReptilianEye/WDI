"""
Zadanie 16. Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5∗17, 8+5 = 5+1+7. Napisać program wypisujący
liczby Smitha mniejsze od 1000000.
"""
from t_14 import is_prime
from math import sqrt


def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def sum_of_factors(l):
    s = 0
    if l == 0:
        return None
    if l == 1:
        return 1
    while l % 2 == 0 or l % 3 == 0:
        if l % 2 == 0:
            l //= 2
            s += 2
        else:
            l //= 3
            s += 3
    i = 6
    while l > 1:
        if l % (i - 1) == 0:
            l //= (i - 1)
            s += sum_of_digits(i-1)
        if l % (i + 1) == 0:
            l //= (i + 1)
            s += sum_of_digits(i+1)
        else:
            i += 6
        if i > sqrt(l) and l != 1:
            s += sum_of_digits(l)
            break
    return s


def f():
    n = 1000
    for l in range(1, n):
        if not is_prime(l):
            if sum_of_digits(l) == sum_of_factors(l):
                print(l, end=", ")


f()
