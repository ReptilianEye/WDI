"""
Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odwa-
żenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
"""


def odwaz(masa, odwazniki, i):
    if masa == 0:
        return True
    if i == len(odwazniki) or masa < 0:
        return False
    # or odwaz(masa - odwazniki[i], odwazniki, i)
    return odwaz(masa, odwazniki, i+1) or odwaz(masa-odwazniki[i], odwazniki, i+1)


"""
Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.
"""


def odwazV2(masa, odwazniki, i):
    if masa == 0:
        return True
    if i == len(odwazniki) or masa < 0:
        return False
    return odwaz(masa, odwazniki, i+1) or odwaz(masa-odwazniki[i], odwazniki, i+1) or odwaz(masa+odwazniki[i], odwazniki, i+1)
    # or odwaz(masa - odwazniki[i], odwazniki, i)


"""
Zadanie 9. Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.
"""


def printOdwazniki(odw, zapalone):
    for i in range(len(odw)):
        if zapalone[i]:
            print(odw[i], end=" ")
    print()


def odwazV3(masa, odwazniki, odw_przyMasie, odw_przeciwMasie, i=0):
    if masa == 0:
        print("przeciw masie: ")
        printOdwazniki(odwazniki, odw_przeciwMasie)
        print("Przy masie")
        printOdwazniki(odwazniki, odw_przyMasie)
        exit()
    if i == len(odwazniki) or masa < 0:
        return

    odwaz(masa, odwazniki, i+1)

    odw_przeciwMasie[i] = True
    odwaz(masa-odwazniki[i], odwazniki, i+1)
    odw_przeciwMasie[i] = False

    odw_przyMasie[i] = True
    odwaz(masa+odwazniki[i], odwazniki, i+1)
    odw_przeciwMasie[i] = True


n = 5
odw_przyMasie = [False for _ in range(n)]
odw_przeciwMasie = [False for _ in range(n)]
odwazV3(20, [2, 4, 6, 9], odw_przyMasie, odw_przeciwMasie)
