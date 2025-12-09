#Pętla while - przykłady

liczba = 120
licznik = 0

#W pętli while podajemy warunek TRWANIA pętli
while liczba > 0: #tak długo jak liczba jest dodatnia, pętla się wykonuje
    liczba = liczba // 2
    licznik = licznik + 1

print(licznik)

#Zadanie 1.
'''x = input('Podaj liczbę lub q aby zakończyć: ')
licznik = 0
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbę lub q aby zakończyć: ')
print(licznik)'''

#Zadanie 2.
popr_haslo = 'informatyka'
haslo = input('Podaj hasło')
proba = 1
while haslo != popr_haslo and proba < 5:
    print('Błędne hasło, podaj raz jeszcze!')
    haslo = input('Podaj hasło')
    proba = proba + 1

if haslo == popr_haslo:
    print('Witaj w systemie :)')
else:
    print('Nie ma hasłą - nie ma dostępu')