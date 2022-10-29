"""
Zadanie 4. Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
"""


def f(n):
    t = [0 for _ in range(n)]
    f = 2  # silnia
    t[0] = 2
    n_iter = 1000
    for i in range(3, n_iter):
        to_divide = 1
        for j in range(n):
            t[j] += to_divide // f
            to_divide = (to_divide % f) * 10
        f *= i
    i = len(t)-1
    while i > 0:
        t[i-1] += t[i] // 10
        t[i] %= 10
        i -= 1
    print(t[0], end=",")
    t[0] = ""
    for el in t:
        print(el, end="")


f(1000)
