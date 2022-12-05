"""
Problem 8 Hetmanow
Jak ustawic na szachownicy 8x8, 8osmiu Hetmanow
"""
import time
Szachownica = [0 for _ in range(8)]

Szachownica = [0, 1, 2, 5, 4, 7, 7, 1]


def czyNaPrzekatnej(w, k, Szachownica):
    for i in range(8):
        if i != k and Szachownica[i] != -1:
            if abs(Szachownica[i] - w) == abs(i-k) or Szachownica[i] == w or i == k:
                return False
    return True


def drukujSzachownice(Szachownica):
    for i in range(8):
        rob = ["." for _ in range(8)]
        for j in range(8):
            if Szachownica[i] == j:
                rob[j] = "*"
        print(*rob)
    print("###########")


def Hetmanow8(Szachownica, k=0):
    if k > 7:
        drukujSzachownice(Szachownica)
        time.sleep(2)
        return
        # exit()

    for w in range(8):
        if czyNaPrzekatnej(w, k, Szachownica):
            Szachownica[k] = w
            Hetmanow8(Szachownica, k+1)
            Szachownica[k] = -1


Hetmanow8([-1 for _ in range(8)])
