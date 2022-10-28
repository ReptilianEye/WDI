"""
Zadanie 6. Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.
"""
from math import sqrt,floor
def f(n):
	if n == 0:  # zero jest przypadkiem brzegowym
		return (0, 0)
	a = floor(sqrt(n))
	while n % a != 0:  # przesuwamy pierwszy dzielnik az do momentu kiedy dzieli n bez reszty
		a = a-1
	b = n // a
	return a, b
