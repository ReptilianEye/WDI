"""
Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
element do sumy elementów wiersza w którym leży element jest największa.
"""
import random

n = 5
T = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
print(T)
def sum_of_col(col):
    s = 0
    for i in range(len(T)):
        s += T[i][col]
    return s

def f(T):
    min_sum_row = 10e10
    min_row = -1
    for r_n,t in enumerate(T):
        s_row = sum(t)
        if min_sum_row > s_row:
            min_sum_row = s_row
            min_row = r_n
    max_sum_col = -1
    max_col = -1
    for col in range(len(T)):
        s_col = sum_of_col(col)
        if max_sum_col < s_col:
            max_sum_col = s_col
            max_col = col

    print(min_row+1,max_col+1)

f(T)