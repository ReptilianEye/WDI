"""
Zadanie 17. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie mu-
szą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb.
"""
#robione kiedys na zajeciach
def is_prime(n):
    if n <2:
        return False
    if n  == 2 or n== 3:
        return True
    if n %2 == 0 or n %3==0:
        return False
    i = 5
    while i*i <=n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return False
