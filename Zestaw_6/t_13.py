"""
Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składni-
ków. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
"""

# counter = 0
# dodanie "i" zabezpiecza nas przed sytuacja w ktorej dodajmy kombinacje nieposortowana
def podziel(n, i=1, komb=""):
    # global counter
    if n == 0:
        print(komb[:-1])
        # counter += 1
        return
    for i in range(i, n+1):
        podziel(n-i, i, komb + str(i) + "+")


podziel(4)
# print(counter)

# Krzysztof Wysocki


# def ff(num, ans, iter=1, s=""):
#     if num == 0:
#         ans.append(s)  # print(s)
#     else:
#         for i in range(iter, num + 1):
#             ff(num - i, ans, i, s + str(i))


# def f(num):
#     ans = []
#     ff(num, ans)
#     return ans


# print(f(5))
