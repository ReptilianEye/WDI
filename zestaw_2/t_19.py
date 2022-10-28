"""
Zadanie 19. Napisać program wczytujący dwie liczby naturalne a,b i wypisujący rozwinięcie dziesiętne
ułamka a/b w postaci ułamka okresowego. Na przykład 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857)
"""


def check_if_rounds(part):
    length = len(part)
    if length % 2 == 1:
        return False
    return part[:length//2] == part[length//2:]


def f(a, b, n=100):
    if a % b == 0:
        return a//b
    result = str(a//b) + '.'
    a = a % b
    floatPart = ""
    i = 1
    while i < n:
        floatPart = floatPart + str(a*10//b)
        a = a*10 - (a*10//b)*b
        i += 1
        if i > 1:
            if check_if_rounds(floatPart):
                result = result + f"({floatPart[:len(floatPart)//2]})"
                return result
    return result + floatPart.strip("0")


print(f(2, 1))
