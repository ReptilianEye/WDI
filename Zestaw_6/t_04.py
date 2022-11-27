"""
Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego.
"""


def pokaz_szachownice(S):
    for w in S:
        for el in w:
            print(el, end=" ")
        print()

skoki = [-2, -1, 1, 2]
def jump_knight(n, w, k, l=1):
    global S
    S[w][k] = l
    for sW in skoki:
        for sK in skoki:
            if abs(sW) != abs(sK):
                if 0 <= w + sW < n and 0 <= k + sK < n and S[w + sW][k+sK] == 0:
                    jump_knight(n, w+sW, k+sK, l+1)


n = 8
S = [[0 for _ in range(8)] for _ in range(n)]
jump_knight(n,0,0)
pokaz_szachownice(S)
