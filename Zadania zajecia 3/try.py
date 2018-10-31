#zadanie 1 

#•	1. Proszę wprowadzić liczbę (funkcja_input), jeżeli liczba jest parzysta - ValueError, jeżeli liczba< 0 - TypeError, jeżeli liczba> 10 - IndexError. Proszę wychwycić wyjątek i powiedzieć użytkowniku w czym jego problem.

#!!! notka dopisac odzyskiwanie exeption
input_number = int(input("podaj liczbe "))
exception_str = ""
try:
	if input_number % 2 == 0:
		raise Exception("ValueError")
		#exception_str = Exception
	elif input_number > 10:
		raise Exception("TypeError")
	elif input_number < 0:
		raise Exception("IndexError")
except:
	print ("wyjatek", exception_str)
	#raise
	
