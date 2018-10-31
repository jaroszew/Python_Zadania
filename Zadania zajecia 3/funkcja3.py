#funkcja 3 nieskonczenie wiele stringów i lacznik

def Combine_String(*args, glue = ":"):
	Combined_String =""
	list_string = []
	for string in args:
		if len(string) > 3 :
			list_string.append(str(string))
	print(list_string)
	Combined_String = glue.join(list_string)
	return Combined_String
	
elements = input ("podaj liste wyrazów oddzielonych przecinkami\r\n")
print (Combine_String(*elements.split(",")))#przekazujemy z * aby przekazas liste jako zbiór osobnych parametrów


