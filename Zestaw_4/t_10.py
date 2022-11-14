"""
Zadanie 10. Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość
True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
False w przeciwnym przypadku.
"""

import random
n = 5
T =[[1 for _ in range(n)] for _ in range(n)]
print(T)
def if_0_in_col(T, col):
    for row in range(len(T)):
        if T[col][row] == 0:
            return True
    return False


def f(T):
    n = len(T)
    for i in range(n):
        if not if_0_in_col(T,i) or not 0 in T[i]:
            return False
    return True


print(f(T))