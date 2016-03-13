class profile:
	
	# metoda przyjmujaca nazwe profilu
	def createNick(self, nick):
		self.nick = nick
	#metoda wyswietlajaca nick profilu
	def displayNick(self):
		return self.nick
    #metoda przyjmujaca wiek kandydata
	def age(self,age):
		self.age = age


	def displayAll(self):
		print "twoj nick to: %s" % self.nick
		print "twoj wiek to %s" % self.age

# zmienna x przyjmuje wartosc wprowadzona z klawiatury
x = raw_input("podaj swoj login\n")


# zmienna x jest teraz nazwa obiektu klasy profile()
x = profile()
# obiekt x przyjmuje metoda createNick i nick przyjmuje wartosc z klawiatury
x.createNick(raw_input("podaj swoj nick\n"))

# wyswietla nick do obiektu x
print x.displayNick()
# wprowadzamy swoj wiek do metody wiek
x.age(raw_input("podaj wiek\n "))

print x.displayAll()
# podaje wiek od ilu do ilu lat
print "Podaj wiek kandydatki: "
od = input("wiek od: ")
do = input("wiek do: ")

przedzial = []
# petla ktora zapisuje kazdy wiek dodajac o jeden wiecej
while od <= do:
	przedzial.append(od)
	od += 1

print przedzial

print "Czy chcesz poznac dopasowane osoby?"



dupa = raw_input("dupa")


