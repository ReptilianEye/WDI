"""
Zadanie 1. Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.
"""
more_sym = ["0", "1", "2", "3", "4", "5", "6",
            "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def f(num, sys):
    num_converted = ""
    while num > 0:
        num_converted = more_sym[num % sys] + num_converted
        num //= sys
    print(num_converted)


f(12, 16)
