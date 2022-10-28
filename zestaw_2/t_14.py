"""
Zadanie 14. Dane są dwie liczby naturalne z których budujemy trzecią liczbę.
W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych.
Wzajemna kolejność cyfr każdej z liczb wejściowych musi być zachowana.
Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd.
Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb.

"""

from math import sqrt, log10, floor


def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6   # jesli sprawdzilismy czy liczba dzieli sie przez 2 i 3 to wystarczy sprawdzac kolejne liczby +1 -1 od 6, bo tylko to sa kandydaci na liczby 1
    while i-1 <= sqrt(n)+1:
        if n % (i-1) == 0:
            return False
        if n % (i+1) == 0:
            return False
        i += 6
    return True


def f(a, b, num=''):
    lenA = floor(log10(a)+1)
    lenB = floor(log10(b)+1)
    N_to_bin = 2**lenA + lenB
    for i in range(N_to_bin):
        bits = ""
        while i > 0:
            if i % 2 == 1:
                bits = bits + "1"
            else:
                bits = bits + "0"
            i //= 2
        if len(bits) < lenA + lenB:
            bits = bits + "0"*(lenA+lenB-len(bits))
        if bits.count("1") == lenA:
            newNum = 0
            a2 = str(a)
            wskA = 0
            b2 = str(b)
            wskB = 0
            for bit in bits:
                newNum *= 10
                if bit == "1":
                    newNum += int(a2[wskA])
                    wskA += 1
                else:
                    newNum += int(b2[wskB])
                    wskB += 1
            if is_prime(newNum):
                print(newNum)
print("Znajduje ile liczb pierwszych mozna zlozyc z dwoch liczb. Jeśli program nic nie wypisze to oznacza że nie ma żadnej takiej liczby.")
f(123,75)
