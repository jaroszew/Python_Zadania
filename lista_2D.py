#lista 2 d
from random import *

number_a = int(input("podaj liczbe a "))
number_b = int(input("podaj liczbe b "))

iterator = int(0)
x =int(0)
list = []
small_list = []
while x != 3:
	while iterator !=4:
		small_list.append(randint(number_a, number_b))
		iterator = iterator + 1
	list.append(small_list)
	x += 1
	

print (list)