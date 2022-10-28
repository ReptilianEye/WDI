"""
Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.
"""

def f(l):
	i = 1
	an = i*i+i+1
	while l > an:
		if l % an == 0:
			print(f"Liczba {l} jest wielokrotnoscia liczby: {an} ktora jest {i}-elementem ciagu i jest jego {l//an}-krotnoscia")
			return
		i += 1
		an = i*i+i+1
	return False
