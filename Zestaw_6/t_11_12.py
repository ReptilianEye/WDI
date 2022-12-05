"""
Zadanie 11. Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym ilo-
czynie.
"""
counter = 0


def nki_o_iloczynie(T, szk_iloczyn,  n_max, iloczyn=1, n=0, i=0):
    global counter
    if i == len(T):
        if iloczyn == szk_iloczyn and n == n_max:
            counter += 1
        return
    if n > n_max:
        return
    nki_o_iloczynie(T, szk_iloczyn, n_max, iloczyn, n, i+1)
    nki_o_iloczynie(T, szk_iloczyn, n_max, iloczyn*T[i], n+1, i+1)


"""
Zadanie 12. Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki
"""


def f(T, szk_iloczyn, n_max):
    final_answ = []

    nki_o_iloczynieV2(T,szk_iloczyn,final_answ,n_max)
    print(*final_answ)


def nki_o_iloczynieV2(T, szk_iloczyn,  final, n_max, temp=[], iloczyn=1, n=0, i=0):
    global counter
    if i == len(T):
        if iloczyn == szk_iloczyn and n == n_max:
            final.append(temp)
            return

    if n > n_max:
        return
    nki_o_iloczynie(T, szk_iloczyn, final, n_max, temp, iloczyn, n, i+1)
    nki_o_iloczynie(T, szk_iloczyn, final,n_max,[*temp,T[i]], iloczyn*T[i], n+1, i+1)

