"""
Zadanie 5. Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
dla 2315 będą to 21, 35, 231, 315.
"""
from math import log10, floor


def f(num):
	digits = (floor(log10(num))+1)
	n_with_enough_bits = 2 ** digits
	for i in range(1, n_with_enough_bits):
		mask = ""
		while i > 0:
			if i % 2 == 1:
				mask =   "1" +mask
			else:
				mask =  "0" +mask
			i //= 2
		if digits > len(mask):
			mask = "0"*(digits-len(mask))+ mask  
		newNum = 0
		wsk = digits
		num2 = num
		for bit in mask:
			if bit == "1":
				newNum = newNum * 10**(wsk) + num2 % 10**wsk
				newNum //= 10**(wsk-1)
			wsk -=1
		if newNum % 7 == 0:
			print(newNum)

f(2315)
