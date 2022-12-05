from math import gcd

"""
Zadanie 1. Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca
licznik, m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie."""


class Root():
    def __init__(self, l, m):
        self.l = l
        self.m = m

    def print(self):
        print(self.l)
        print("-")
        print(self.m)
        print()

    def simplify(self):
        div = gcd(self.l, self.m)
        self.l = self.l//div
        self.m = self.m//div

    def add(self, b):
        self.l = self.l * b.m + b.l * self.m
        self.m = b.m * self.m
        self.simplify()

    def sub(self, b):
        self.l = self.l * b.m - b.l * self.m
        self.m = b.m * self.m
        self.simplify()

    def multi(self, b):
        self.l = self.l * b.l
        self.m = self.m * b.m
        self.simplify()

    def div(self, b):
        self.l = self.l * b.m
        self.m = self.m * b.l
        self.simplify()

    def power(self, pow):
        self.l **= pow
        self.m **= pow
