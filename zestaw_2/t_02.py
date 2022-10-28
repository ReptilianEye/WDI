"""
Zadanie 2. Napisać program wczytujący trzy liczby naturalne a, b, n i wypisujący rozwinięcie dziesiętne
ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)
"""
def f(a,b,n):
    i = 0
    if a > b:
        wartoscUlamka = str(a//b)
    else:
        wartoscUlamka = "0"
    wartoscUlamka = wartoscUlamka + ","
    a = (a % b) * 10

    while i < n:
        wartoscUlamka = wartoscUlamka + str(a//b)
        a = (a % b) * 10
        i += 1
    print(wartoscUlamka)
    return wartoscUlamka