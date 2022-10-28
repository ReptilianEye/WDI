"""
Zadanie 10. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz
jest równy 2.
"""

def f(num):
    if num % 2==0:  # sprawdza czy num jest wielkrotnoscia a1=2
        return True 
    an = 7 # 3 * a1 (z tresciz adania=2) + 1
    while an <= num:
        if num % an==0:
            return True
        an = 3*an+1
        print(an," ")
    return an