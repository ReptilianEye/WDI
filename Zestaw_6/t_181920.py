"""
Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
narożnika.
Zadanie 19. Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z pola w,k do którego-
kolwiek z narożników.
Zadanie 20. Zadanie jak powyżej. Funkcja powinna dostarczyć drogę króla w postaci tablicy zawierającej
kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu.
"""

import random
from math import log10, floor


def krol(w, k, T):
    def sprawdz_krok(w, k, n_w, n_k, koniec, T):
        if w+n_w > len(T) or w+n_w < 0 or k+n_k > len(T) or k+n_k < 0:
            return False
        if T[w][k] % 10 >= T[w+n_w][k+n_k] // 10 ** floor(log10(T[w+n_w][k+n_k])):
            return False
        if abs(koniec[0] - w+n_w) > abs(koniec[0] - w) or abs(koniec[1] - k+n_k) > abs(koniec[1] - k):
            return False
        return w+n_w, k+n_k

    def krol_r(w, k, T, path, i=0, koniec=(7, 7)):
        nonlocal success
        if w == koniec[0] and k == koniec[1]:
            success = True
            exit()
        krok_n = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 and j != 0:
                    resp = sprawdz_krok(w, k, i, j, koniec, T)
                    if resp:
                        path[i] = krok_n
                        krol_r(resp[0], resp[1], T, path, i+1)
                    krok_n += 1
    path = [-1 for _ in range(len(T)*2)]
    success = False
    krol_r(w, k, T, path)
    if success:
        return path
    return success


n = 8
T = [[random.randint(1, 100) for _ in range(n)]for _ in range(n)]
print(krol(0, 0, T))
