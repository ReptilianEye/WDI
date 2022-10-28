"""
Zadanie 15. Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr
liczby jest równa tej liczbie, np. 153 = 13 + 53 + 33
"""
from math import log10,floor

def sum_of_N_powers(num):
    sum = 0
    power = floor(log10(num))+1
    while num != 0:
        sum += (num%10)**power
        num //=10
    return sum

def f(n):
    i = 10**(n-1)
    for i in range(i,i*10):
        if i == sum_of_N_powers(i):
            print(i)
