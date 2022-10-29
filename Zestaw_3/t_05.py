"""
Zadanie 5. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.
"""

# moje rozwizanie


def f():
    dane = []
    wejscie = int(input(
        "Podaj liczbe naturalną. Jeśli chcesz skończyć wpisywać dane, napisz '0'. Program zwróci 10 co do wielkosci liczbe"))
    while wejscie != 0:
        dane.append(wejscie)
        wejscie = int(input())
    dane.sort(reverse=True)
    print(dane[10])


# rozwiazanie z cwiczen
def min_index(t):
    min_v = 1e10
    min_i = -1
    for i in range(len(t)):
        if min_v > t[i]:
            min_v = t[i]
            min_i = i
    return min_i


def contain(t, v):
    for el in t:
        if el == v:
            return True
    return False


def fV2():
    t = [-1 for _ in range(10)]
    print("Program zwróci 10 co do wielkosci liczbe.")
    w = int(input(
        "Podaj liczbe naturalną. Jeśli chcesz skończyć wpisywać dane, napisz '0':  "))
    while w != 0:
        if not contain(t, w):
            poz_min = min_index(t)
            if t[poz_min] < w:
                t[poz_min] = w
        w = int(input(
            "Podaj liczbe naturalną. Jeśli chcesz skończyć wpisywać dane, napisz '0': "))
    min_v = 1e10
    for el in t:
        min_v = min(el, min_v)
    print(min_v)


fV2()
