# Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry.
# Proszę napisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu(w zakresie
# 2-16) w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
# taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
# podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11)

moreDigits = {10: "A",
              11: "B",
              12: "C",
              13: "D",
              14: "E",
              15: "F"}


def convert_to_sys(num, sys):
    num_in_sys = ""

    while num > 0:
        newDig = num % sys

        if newDig > 9:
            newDig = moreDigits.get(newDig)

        num_in_sys = str(newDig) + num_in_sys
        num //= sys
    return num_in_sys


def check_if_nums_have_unique_digits(a, b):
    a = str(a)
    b = str(b)
    for el in a:
        if el in b:
            return False
    return True


def f(a, b):
    if check_if_nums_have_unique_digits(a, b):
        return a, b
    for i in range(2, 17):
        a2 = convert_to_sys(a, i)
        b2 = convert_to_sys(b, i)
        if check_if_nums_have_unique_digits(a2, b2):
            print(
                f"Liczby {a}, {b} maja liczby o wzajemnie unikalnych cyfrach dla postaci {i}", a2, b2)
            return
