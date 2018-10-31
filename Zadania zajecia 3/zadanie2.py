#zadanie 2

#zadana lista 

List_of_elements = [1,"str",["a","b","c"],"Lipa", 42, -1]

print ("witaj oto lista " +str(List_of_elements) +" skalada sie ona z " + str(len(List_of_elements)) + " elementow.(numerowane od 0 do " +str(len(List_of_elements)-1)+")")
If_Continue ="T"

while If_Continue == "T": 
	intput_index = input ("ktory element wyswietlic?\r\n")
	try:
		print(List_of_elements[intpur_index])
	except:
		print ("nie ma takiego elelemtu")
	If_Continue = input("kontunuowac? \r\n T -tak\r\n N -nie\r\n").upper()
		