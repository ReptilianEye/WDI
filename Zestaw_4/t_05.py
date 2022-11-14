"""
Zadanie 5. Poprzednie zadanie z tablicą wypełnioną liczbami całkowitym
"""
import random

#Unfinished!!!!!!!!!!!!!!

n = 5
T = [[random.randint(-50, 50) for _ in range(n)] for _ in range(n)]
print(T)


def sum_of_col(col):
    s = 0
    for i in range(len(T)):
        s += T[i][col]
    return s


def f(T):
    min_sum_row = 10e10
    min_row = -1

    min_poz_sum_row = -1
    min_poz_row = -1
    for r_n, t in enumerate(T):
        s_row = sum(t)
        if s_row > 0 and min_poz_sum_row > s_row:
            min_poz_sum_row = s_row
            min_poz_row = r_n
        if min_sum_row > s_row:
            min_sum_row = s_row
            min_row = r_n

    max_sum_col = -1
    max_col = -1
    min_sum_col = 10e10
    min_col = -1
    for col in range(len(T)):
        s_col = sum_of_col(col)
        if min_sum_col > s_col:
            min_poz_sum_row = s_col
            min_col = col
        if max_sum_col < s_col:
            max_sum_col = s_col
            max_col = col

    if min_sum_row < 0 and min_sum_col < 0:
        if min_sum_col/min_sum_row > max_sum_col/min_poz_sum_row:
            print(min_row, min_col)
        else:
            print(min_poz_row, max_col)
    elif max_sum_col < 0:
        print(min_row, min_col)
    else:
        print(min_poz_row, max_col)


f(T)
