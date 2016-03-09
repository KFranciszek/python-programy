print "      Witam w moim kalkulatorze     "
print "------------------------------------"
print "prosze wybrac operacjne matematyczna"
print "1) dodawanie"
print "2) odejmowanie"
print "3) mnozenie"
print "4) dzielenie"
print "5) wyjscie z programu"
choose=input("wybor: ")

if choose == 1:
	print "wybrales dodawanie, wprowadz dwie liczby"
	liczba1 = input("liczba pierwsza: ")
	liczba2 = input("liczba druga: ")
	print liczba1 + liczba2
	dupa = input("koniec")
elif choose ==2:
	print "wybrales odejmowanie,wprowadz dwie liczby"
	liczba1 = input("liczba pierwsza: ")
	liczba2 = input("liczba druga: ")
	print liczba1 - liczba2
	dupa = input("koniec")
elif choose ==3:
	print "wybrales mnozenie, wprowadz dwie liczby"
	liczba1 = input("pierwsza licza: ")
	liczba2 = input("druga liczba: ")
	print liczba1 * liczba2
	dupa = input("koniec")
elif choose ==4:
	print "wybrales dzielenie,wprowadz dwie liczby"
	liczba1 = input("liczba pierwsza: ")
	liczba2 = input("liczba druga: ")
	print liczba1 / liczba2
	dupa = input("koniec")
