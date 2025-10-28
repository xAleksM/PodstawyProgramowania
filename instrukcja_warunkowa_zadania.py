#Rozwiązywanie równania kwadratowego
# a = float(input('Podaj liczbę a =/= 0'))
# b = float(input('Podaj liczbę b'))
# c = float(input('Podaj liczbę c'))
#
# delta = b ** 2 - 4 * a * c
#
# if delta > 0:
#     x1 = (-b - delta ** 0.5) / (2 * a)
#     x2 = (-b + delta ** 0.5) / (2 * a)
#     print(f'x1 = {x1} v x2 = {x2}')
# elif delta == 0:
#     x = (-b) / (2 * a)
#     print('x1 = x2 = {}'.format(x))
# else:
#     print('brak rozwiązań')

# Zadanie 12.
pisemny_j_polski = int(input('pisemny polski'))
pisemny_j_obcy = int(input('pisemny obcy'))
pisemny_j_dodatkowy = int(input('pisemny dodatkowy'))
ustny_j_polski = int(input('ustny polski'))
ustny_j_obcy = int(input('ustny obcy'))

if pisemny_j_polski >= 30 and pisemny_j_obcy >= 30 and pisemny_j_dodatkowy >= 30\
        and ustny_j_polski >=30 and ustny_j_obcy >30:
    print('Zdałeś bez amnestii')
elif (pisemny_j_polski + pisemny_j_obcy + pisemny_j_dodatkowy + ustny_j_polski + ustny_j_obcy) / 5 >=30:
    print('Zdałeś z amnestią')
else:
    print('nie zdałeś!')

    # zadanie 13
    '''Klasa ma być podzielona na dwie grupy, w zależności od wyniku testu kompetencji
    językowych z wybranego języka obcego lub oceny na świadectwie ukończenia szkoły
    podstawowej. Jeśli dany uczeń uzyskał z testu wynik powyżej 90% punktów lub jeśli
    na świadectwie ukończenia szkoły podstawowej miał z danego języka ocenę nie
    niższą niż 5, to kwalifikuje się do grupy zaawansowanej. W przeciwnym wypadku
    kwalifikuje się do grupy podstawowej. Napisz specyfikację zadania oraz stwórz
    program sprawdzający, do jakiej grupy zakwalifikuje się dany uczeń. Liczbę punktów
    uzyskanych z testu i ocenę ze świadectwa wprowadzaj z klawiatury, a komunikat:
    „grupa zaawansowana” lub „grupa podstawowa” wyświetlaj na ekranie.'''

    # zmienne sprawdzające wyniki ucznia

    ocena = int(input('Podaj ocenę z wybranego języka obcego: '))
    test = int(input('Podaj wynik z testu kompetencji językowych wybranego języka obcego: '))

    # skrypt sprawdza do jakiej grupy dostanie się uczeń
    # jeśli sprawdzający zrobi błąd to program poda wynik
    # na podstawie drugiej wartości a jeżeli będą 2 błędy
    # to poprosi o spóbowanie ponownie

    if (ocena >= 5 and ocena <= 6) or (test >= 90 and test <= 100):
        print('Grupa zaawansowana')
    elif (ocena >= 1 and ocena <= 4) or (test >= 0 and test <= 89):
        print('Grupa podstawowa')
    else:
        print('Sprawdż czy podałeś poprawnygi wynik z testu i ocenę')

    # zadanie 14

    a = float(input('Podaj pierwszą liczbę różną od zera: '))
    b = float(input('Podaj drugą liczbę: '))
    c = float(input('Podaj trzecią liczbę: '))

    print('ax² + bx + c =0')

    if a == 0:
        print('Współczynnik a powinien być różny od 0')
    elif b == 0 and c == 0:
        print('ax² = 0')
        print('x₀ = 0')
    elif b == 0:
        print('x² + c = 0')
        if (-c / a) > 0:
            print('równanie ma dwa rozwiązania: 𝑥₁ = √(-c/a) lub x₂ = -√(-c/a)')
            x1 = (-c / a) ** 0.5
            x2 = -(-c / a) ** 0.5
            print(f'x₁ = {x1}, x₂ = {x2}')
        else:
            print('równanie nie ma rozwiązań (jest sprzeczne)')
    elif c == 0:
        print('równanie ma dwa rozwiązania: x₁ = 0 lub x₂ = (-b/a)')
        x1 = 0
        x2 = (-b / a)
        print(f'x₁ = {x1}, x₂ = {x2}')
    else:
        delta = (b ** 2) - 4 * (a * c)
        if delta > 0:
            print(
                'równanie ma dwa rozwiązania: 𝑥₁ = (-b + (delta ** 0.5) / (2 * a) lub x₂ (-b - (delta ** 0.5) / (2 * a))')
            x1 = (-b + (delta ** 0.5)) / (2 * a)
            x2 = (-b - (delta ** 0.5)) / (2 * a)
            print(f'x₁ = {x1}, x₂ = {x2}')
        elif delta == 0:
            print('x₀ = (-b) / (2 * a)')
            x0 = (-b) / (2 * a)
            print(f'x₀ {x0}')
        else:
            print('równanie nie ma rozwiązań')