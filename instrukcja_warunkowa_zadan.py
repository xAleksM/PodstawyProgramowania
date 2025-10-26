#zadanie 13
'''Klasa ma być podzielona na dwie grupy, w zależności od wyniku testu kompetencji
językowych z wybranego języka obcego lub oceny na świadectwie ukończenia szkoły
podstawowej. Jeśli dany uczeń uzyskał z testu wynik powyżej 90% punktów lub jeśli
na świadectwie ukończenia szkoły podstawowej miał z danego języka ocenę nie
niższą niż 5, to kwalifikuje się do grupy zaawansowanej. W przeciwnym wypadku
kwalifikuje się do grupy podstawowej. Napisz specyfikację zadania oraz stwórz
program sprawdzający, do jakiej grupy zakwalifikuje się dany uczeń. Liczbę punktów
uzyskanych z testu i ocenę ze świadectwa wprowadzaj z klawiatury, a komunikat:
„grupa zaawansowana” lub „grupa podstawowa” wyświetlaj na ekranie.'''

#zmienne sprawdzające wyniki ucznia

ocena = int(input('Podaj ocenę z wybranego języka obcego: '))
test = int(input('Podaj wynik z testu kompetencji językowych wybranego języka obcego: '))

#skrypt sprawdza do jakiej grupy dostanie się uczeń
#jeśli sprawdzający zrobi błąd to program poda wynik
#na podstawie drugiej wartości a jeżeli będą 2 błędy
#to poprosi o spóbowanie ponownie

if (ocena >= 5 and ocena <= 6) or (test >= 90 and test <=100):
    print('Grupa zaawansowana')
elif (ocena >= 1 and ocena <= 4) or (test >= 0 and test <= 89):
    print('Grupa podstawowa')
else:
    print('Sprawdż czy podałeś poprawnygi wynik z testu i ocenę')