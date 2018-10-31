#definiowanie funkcji
#def to słówko kluczowe do definiowania funkcji


def my_function (Input_String, Flag = True):
	if Flag == True:
		return Input_String.upper()
	else:
		return Input_String.lower()

print (my_function ("la la la", True))