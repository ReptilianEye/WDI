"""
Zadanie 4. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
2, 3, 5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
od 1 do N włącznie.
"""
def f(n):
	a = 1
	counter = 0
	while a <= n:
		b = a
		while b <= n:
			c = b
			while c <= n:
				counter += 1
				c = c*5
			b = b * 3
		a = a * 2
	return counter

def gen_235num(n):
    q = [1]
    i = 0
    t = [5, 3, 2]

    while i < len(q):
        w = q[i]
        for x in t:
            if (x*w <= n):
                # liczbe zwiekszoną 5-krotnie zawsze dodamy (jesli <n)
                q.append(x*w)
            if (w % x == 0):
                # jesli w jest krotnoscia 5 (lub w kolejnej petli 3) to nie będziemy dalej iterowali dla mniejszych wartosci od 5 (potem 3)
                break
        i += 1
    q.sort()
    return q
