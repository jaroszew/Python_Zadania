#pole prostokoata

side_a = input("podaj bok a ")
side_b = input("podaj bok b ")

wynik = float(side_a)*float(side_b)

if float(side_a) == float(side_b):
	print ("pole " + str(wynik) + " to jest kwadrat")
else:
	print ("pole " + str(wynik))