#funkcja 1 znajdź min oraz max

def FindMinAndMax(*arg):
	Max = max(*arg)
	Min = min(*arg)
	return Min,Max
	
elements = input ("podaj liste cyfr oddzielonych przecinkami\r\n")
print (FindMinAndMax(elements.split(",")))


