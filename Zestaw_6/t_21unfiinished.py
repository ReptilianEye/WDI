"""
Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
wartość sumy, funkcja powinna zwrócić wartość typu bool
"""
# uznaje że zadanie sprowadza się do ustawienia wiezy w taki sposob że pola na których stoją razem będą równe
# zadanej sumie i wieże nie mogą się szachować


def wieze(T, s):
    def wiezeOSumie_r(T, uzyte_wiersze, szuk_s, k=0, s=0):
        n = len(T)
        nonlocal success
        if s == szuk_s:
            success = True
            exit()
        if k == n:
            return
        for i in range(n):
            if not uzyte_wiersze[i]:
                uzyte_wiersze[i] = True
                wiezeOSumie_r(T, uzyte_wiersze, szuk_s, k+1, s+T[i][k])
                uzyte_wiersze[i] = False
            wiezeOSumie_r(T, uzyte_wiersze, szuk_s, k+1, s)

    def wiezeOSumie_rV2(T, visited, szuk_s, w=0, k=0, s=0):
        n = len(T)
        if k == n:
            return s == szuk_s
        

    

    success = False
    uzyte_wiersze = [False for _ in range(len(T))]
    wiezeOSumie_r(T,uzyte_wiersze,s)
    return success

T = [[1 for _ in range(5)]for _ in range(5)]
print(wieze(T,2))
