#liczny pierwsze metoda sita

number = input("podaj liczbe ")
wynik = 0
list = []
found = False

for x in range (0,int(number)+1):
	#found = False
	if int(x) == 0:
		pass
	elif int(x) == 1:
		pass
	elif int(x) == 2:
		list.append(int(x)) #jak dwa dodaj ją do listy
	else:
		for prime in list: #sprawdx czy liczba dzieli sie przez liczby pierwsze na liscie pierwszych
			if int(x) % int(prime)== 0:
				found = True
		if found == False:
			list.append(int(x))
	found = False
	x = int(x) + 1

print (list)