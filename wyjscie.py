#1. Co można wyświetlać printem?
print(5)
print((2+2)*2)

x = 34

print(x)

print('informatyka')
print(round(2.234, 2))
print(2 == 3 and 1 > 0)
print([6, 1, 9, 4, 2])

#2. formatowanie wyświetlania tekstu

imie = input('Podaj imię')
nazwisko = input('Podaj nazwisko')
wiek = int(input('Podaj swój wiek'))

#sposób 1
'''print('Witaj ' + imie + ' ' + nazwisko + '. Masz ' + str(wiek) + ' lat. Za 5 lat będziesz mieć ' + str(wiek + 5) + ' lat ')'''

#sposób 2
'''print(f'Witaj {imie} {nazwisko}. Masz {wiek} lat. Za 5 lat będziesz mieć {wiek + 5} lat')'''
liczba = 4.1237
print(f'Kwota = {liczba: 0.3f}')

#sposób 3.1
print('Witaj {} {}. Masz {} lat. Za 5 lat będziesz mieć {} lat.'.format(imie, nazwisko, wiek, wiek +5))

#sposób 3.2
print('Witaj {1} {0}. Masz {2} lat. Za 5 lat będziesz mieć {3} lat.'.format(nazwisko, imie, wiek, wiek +5))