#quiz
from random import *

asked_questions = []
list_current_questions = [
["czy obiekt typu lista posiada funkcje sortujace?","TRUE"],
["integer(), string() to funkcje do rzutowania typu?","FALSE"],
["czy mozna zwrocic dlugosc listy?","TRUE"],
["Wersja Pythona nie ma wplywu na wykonywalny kod","FALSE"],
["w Pythonie 2.7 przy wykonywaniu dzialan na intach jezeli wynik bedzie niecalkowity to zostanie on przekonvertowany?","FALSE"],
["czy slownik moze miec powtarzajace sie wartosci kluczy?","FALSE"],
["czy slownik moze zawierac powtarzajace sie wartosci?","TRUE"],
["czy za pomoca slownik[key] = wartosc mozemy zarowno dodac nowa wartosc jak i zmienic istniejaca w danym kluczu?","TRUE"],
["czy do slownika mozna dodac nowy element?","TRUE"],
["czy z tulpy mozna usuwac elementy?","FALSE"],
["czy mozna modyfikowac elementy w liscie?","TRUE"],
["czy mozna uzyc petli for na liczbach z podanego zakresu?","TRUE"],
["czy tulpe mozna posotrowac?","FALSE"],
["czy zmienna number_a bedzie taka sama niezalerznie czy przypiszemy do niej wartosc number_a = int(input(podaj liczbe a )) oraz number_a = input(podaj liczbe a ) ?","FALSE"],
["czy  mozna stosowac zamiennie  wyrazenia wynik = wynik + 1 i wynik += 1","TRUE"],
["wyrazenie list[len(list)-1] zwruci ostatni element z listy?","TRUE"],
["czy jezeli stworzymy liste= [A,B,C] i ustalimy string = * to jako wynik dzialanie string.join(list) otrzymamy ciag A*B*C?","TRUE"],
["czy mozna zostawic pusta linike pod if, elif oraz else tak aby program nie wykonywal zadnej operacji?","FALSE"], #pusta nie moze byc musi byc podane pass
["czy string posiada metode spit()?","TRUE"],
["czy string posiada metode append()?","FALSE"],
["czy w print mozna laczyc ze soba rozne typy bez rzutowania?","FALSE"],
]

anwser =""
int_score = 0
int_empty = 0
selected_question_number = 0
while len(asked_questions) < 10:
	selected_question_number = randint(0, len(list_current_questions)-1)
	if selected_question_number not in asked_questions:
		asked_questions.append(selected_question_number)
		print("\r\n"+list_current_questions[selected_question_number][0])
		anwser = input("true czy false \r\n")
		if anwser == "":
			int_empty += 1
			print ("poprawana odpowiedz "+ list_current_questions[selected_question_number][1])
		if anwser.upper() == list_current_questions[selected_question_number][1]:
			int_score += 1
			print ("poprawana odpowiedz "+ list_current_questions[selected_question_number][1])
print ("\r\ntwoj wynik " +str(int_score)+"\r\nWynik w % " + str(int_score/len(asked_questions)*100) + "\r\npominiete " + str(int_empty))