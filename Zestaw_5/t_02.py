"""
Zadanie 2. Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2 równań
o 2 niewiadomych.
"""
from t_01 import Root
#metoda wyznacznikow


#dane:
# {
# ax + by = c 
# dx + ey = f
# }
# --> dane = [a,b,c,d,e,f] 

def solv_2_var(dane):
    W = dane[0]*dane[4] - dane[1]*dane[3]
    Wx = dane[2]*dane[4] - dane[1]*dane[5]
    Wy = dane[0]*dane[5] - dane[2]*dane[3]
    return Wx/W,Wy/W
