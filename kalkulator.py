#zadanie 3 kalkulator

guide = "witaj, w kalkulatorze. Mozesz wykonywac ponizsze operacje:\r\n + odawanie\r\n - odejmowanie \r\n * mnozenie\r\n / dzielenie \r\n = podaj wynik \r\n C wyczysc"
print (guide)
operation_list = []
wynik = 0
number = 0
last_number = 0
last_operation =""

operation = input("wpisz operacje\r\n")

while operation != "=":
	operation_list.append(operation)
	if operation == "C":
		operation_list.clear
		wynik = 0
	else:
		if operation.isdigit():
			number = operation
			if len(operation_list) == 1:
				wynik = number
			if last_operation == "*":
				wynik = float(wynik) * float(number)
			elif last_operation == "+":
				wynik = float(wynik) + float(number)
			elif last_operation == "-":
				wynik = float(wynik) - float(number)
			elif last_operation == "/":
				if number == "0":
					print("nie mozna wykonac operacji")
				else:
					wynik = float(wynik) / float(number)
			elif last_operation == "=":
				wynik
		else:
			last_operation = operation
	print ("obecny wynik " +str(wynik))
	operation = input("wpisz operacje\r\n")
		
operation_list.append(operation)

print("\r\ntwoje operacje " + str(operation_list))
print("finalny wynik " + str(wynik))
