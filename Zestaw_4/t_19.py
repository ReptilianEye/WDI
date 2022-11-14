"""
Zadanie 19. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
szachowego.
"""
def f(T,il):
    n = len(T)
    c = 0
    for i in range(n-1):
        for j in range(n-1):
            if i+2 < n and j+1 < n:
                if T[i][j] * T[i+2][j+1] == il:
                    c += 2
            if i+1 < n and j+2 < n:
                if T[i][j] * T[i+1][j+2] == il:
                    c += 2
            if i-1 >= 0 and j+2 < n:
                if T[i][j] * T[i-1][j+2] == il:
                    c += 2
            if i+1 < n and j-2 >= 0:
                if T[i][j] * T[i+1][j-2] == il:
                    c += 2
    print(c)