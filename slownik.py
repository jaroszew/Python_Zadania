#slownik zadanie 6

Dictonaty = {}

while len(Dictonaty) <= 5:
	input_key = input("podaj klucz ")
	if input_key in Dictonaty:
		input_key = input("klucz jest w slowniku, podaj nowy klucz ")
	input_value = input("podaj wartosc ")
	Dictonaty[input_key] = input_value

print (Dictonaty)
	