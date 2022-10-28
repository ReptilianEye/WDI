"""
Zadanie 11. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
jej cyfry stanowią ciąg rosnący.
"""

def f(num):
    prev = num%10 + 1
    while num != 0:
        last_dig = num%10
        if last_dig >= prev:
            return False
        prev = last_dig
        num //= 10
    #end
    return True
