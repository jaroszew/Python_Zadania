#wygeneruje pseudolosowe inty z danego przedziału
from random import *

number_a = int(input("podaj liczbe a "))
number_b = int(input("podaj liczbe b "))

iterator = int(0)
list = []
while iterator != 6:
	list.append(randint(number_a, number_b))
	iterator = iterator + 1
	
#sortuj liczby
list.sort()
			
print (list)