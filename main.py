#wytłumaczenie zadania 5 z grupy A w kartkówce

dane = input('Podaj 5 liczb')
lista = dane.split(';')
print(lista)

wynik = ''

if int(lista[0]) > 0:
    wynik = wynik + lista[0]
if int(lista[1]) > 0:
    wynik = wynik + ',' + lista[1]
if int(lista[2]) > 0:
    wynik = wynik + ',' + lista[2]
if int(lista[3]) > 0:
    wynik = wynik + ',' + lista[3]
if int(lista[4]) > 0:
    wynik = wynik + ',' + lista[4]

print(wynik)

#Kolejne zadanie z kartkówki

wyraz = 'amteytkaam'
print(wyraz[::-2] + wyraz[::2])
