# zadanie 14 lista z to delete

list = []

while len(list) !=10:
	x = int(input("podaj liczne z przedzialu 1 - 10 "))
	if x >0 and x < 11:
		if x not in list:
			list.append(x)
		else:
			print("liczba jest juz w liscie")

list.sort()
list.reverse()
print ("lista finalna to")
print (list)