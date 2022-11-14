"""
Zadanie 20. Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
wież. Uwaga - zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi.
"""

T = []


def sum_of_col(col):
    s = 0
    for i in range(len(T)):
        s += T[i][col]
    return s


def f(T):
    max_col = -1
    max_row = -1
    i_max = -1
    j_max = -1

    s_max_col = -1
    s_max_row = -1
    i_s_max = -1
    j_s_max = -1

    for i in range(len(T)):
        sum_row = sum(T[i])
        sum_col = sum_of_col(i)

        if max_col < sum_col:
            s_max_col = max_col
            j_s_max = j_max
            max_col = sum_col
            j_max = i
        elif s_max_col < sum_col:
            s_max_col = sum_col
            j_s_max = i

        if max_row < sum_row:
            s_max_row = max_row
            i_s_max = i_max
            max_row = sum_row
            i_max = i
        elif s_max_row < sum_row:
            i_max_row = sum_row
            i_s_max = i

    print()