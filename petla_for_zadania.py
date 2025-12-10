from math import inf
#inf - bardzo duża liczba
#Zadanie 15
'''X = list(range(3, 103, 3))'''

'''print(f'x\ty')
for x in X:
    y= 0.5 * x + 3
    #print(x, y)
    print(f'{x}\t{y}')'''

#b)

print(f'x\ty')
for x in range(-30, 61):
    x = x / 10
    y = 0.5 * x + 3
    if x >= 0:
        print(f'{x}\t{y}')
else:
    print(f'{x}\t{y}')

#zadanie 16
lista1 = list(range(3,31, 3))
lista2 = list(range(11,111, 11))
lista3 = list(range(13,131, 13))

#sposob 1
'''for x, y ,z in zip(lista1, lista2, lista3):
    print(f'{x}\t{y}\t{z}')'''

#sposob 2
'''for i in range(10):
    print(f'{lista1[i]}\t{lista2[i]}\t{lista3[i]}')'''

'''lista10 = [10, 56, 89, 59]'''

'''for q in lista10:
    print(q)'''

'''for i in range(len(lista10)):
    print(i)'''

#zadanie 17
n = int(input('Podaj ile będzie liczb'))
suma = 0
max_liczba = -inf
min_liczba = inf #plus nieskończoność
ile_mnienj_3 = 0
ile_przedzial = 0

for x in range(n):
    liczba = int(input('Podaj liczbę'))
    suma = suma + liczba
    if liczba > max_liczba:
        max_liczba = liczba
    if liczba < min_liczba:
            min_liczba = liczba
    if liczba < 3:
        ile_mnienj_3 = ile_mnienj_3 + 1
    if liczba > -2 and liczba >= 11:
        ile_przedzial = ile_przedzial + 1
print(suma)
print(suma / n)
print(max_liczba)
print(min_liczba)
print(ile_mnienj_3)
print(ile_przedzial)
lista = []
for x in range(n):
    liczba = int(input('Podaj liczbę'))
    lista.append(liczba)
print(sum(lista))
print(sum(lista) / n)
print(max(lista))
print(min(lista))