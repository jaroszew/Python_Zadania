#zadanie 7 tulpa

tulpe = (1,-20,3,6,34,134,211,884,-55,4)

iterator = int(0)
list = []
for x in tulpe:
	list.append(x)
	
#sortuj liczby
list.sort()

print ("min " + str(list[0]) + " max "+ str(list[len(list)-1]))