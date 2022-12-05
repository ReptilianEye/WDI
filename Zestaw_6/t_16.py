"""
Zadanie 16. Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę sa-
mogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład ′′ula′′→117, 108, 97
1
oraz ′′exe′′→101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowa-
nie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna wypisać
znaleziony wyraz.
"""
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']


def waga_s(s):
    w_s = 0
    for char in s:
        w_s += ord(char)
    return w_s


def ile_samo(s):
    n_samo = 0
    for char in s:
        n_samo += 1
    return n_samo


def znajdz_wage(s1, s2):
    def znajdz_wage_r(s, waga, n_samo, i=0, rob=""):
        if waga == 0:
            print(rob)
            return
        if waga < 0 or i >= len(s):
            return
        znajdz_wage_r(s, waga, n_samo, i+1, rob)
        if s[i] in samogloski:
            samo = 1
        else:
            samo = 0
        znajdz_wage_r(s, waga-ord(s[i]), n_samo - samo, i+1, rob+s[i])

    waga_s1 = waga_s(s1)
    waga_s2 = waga_s(s2)
    if waga_s2 < waga_s1:
        return False

    samo_s1 = ile_samo(s1)
    samo_s2 = ile_samo(s2)
    if samo_s2 < samo_s1:
        return False
    znajdz_wage_r(s2, waga_s1, samo_s1)


znajdz_wage("ula", "exe")
