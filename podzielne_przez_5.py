#liczby pidzielne przez 5 w przedziale

number_a = int(input("podaj liczbe a "))
number_b = int(input("podaj liczbe b "))

list = []


for number in range (number_a,number_b+1):
	if number % 5 ==0:
		list.append(number)

print (list)