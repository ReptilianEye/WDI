"""
Zadanie 9. Napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale od 1
do k, metodą prostokątów.
"""

def f(n,slicers = 10e6):
    step = (n-1)/slicers
    i = 1
    area = 0
    while i < n:
        area += 1/i
        i += step
    return area

print(f(100))