"""
Zadanie 14. Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
wartości prawdopodobieństwa dla N z zakresu 20-40.
"""
import time
from random import randint
# problemem jest że liczby nie są tak naprawde generowane randomowo, a są zależne od czasu. Przez to lepiej aby liczby generowane były mniej częstotliwie


def gen_t(n, time_step=1):
    t = []
    for _ in range(n):
        t.append(randint(1, 365))
        time.sleep(time_step)
    return t


def f(n):
    to_repeat = 1000
    success = 0
    for _ in range(to_repeat):
        t = gen_t(n)
        # t = [randint(1, 365) for _ in range(n)] #randint generuje bardzo dużo powtórek bo sie za szybko tworzy
        # print(t)
        if len(t) != len(set(t)):
            success += 1

    print(success/to_repeat)


f(20)
