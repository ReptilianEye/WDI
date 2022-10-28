"""
Zadanie 13. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba zakończona jest unikalną cyfrą.
"""

def f(num):
    last_dig = num%10
    num//=10
    while num > 0:
        if num %10 == last_dig:
            return False
        num //=10
    return True

