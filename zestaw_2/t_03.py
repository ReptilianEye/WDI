"""
Zadanie 3. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.
"""

# Jesli liczba jest palindromem to rewers tej liczby jest rowny tej liczbie
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev*10+n % 10
        n = n//10
    return rev


def n_to_bin(n):
    wart = 9
    # z obu stron liczby dodamy 9 jako wartowniki (aby zawzec wiodace zera) (na potrzeby programu)
    bin_num = wart
    while n > 0:
        bin_num *= 10
        bin_num += n % 2
        n //= 2
    bin_num = bin_num * 10 + wart
    return bin_num


def f(n):
    if n == reverse(n):
        if n_to_bin(n) == reverse(n_to_bin(n)):
            print(
                f"Liczba {n} jest palindomem w postaci dziesietnej i dwójkowej")
        else:
            print(f"Liczba {n} nie jest palindomem w postaci dwójkowej")
    else:
        print(f"Liczba {n} nie jest palindomem w postaci dziesietnej")

