lista = [12, 45, 78, 101, 9, -5, 9, 7, 23]

#Zadanie 2. gr B
#sposób 1
'''for i in range(len(lista)):
    if i % 2 == 1:
        print(lista[i])'''

#sposób 2
'''for i in range(1, len(lista), 2):
    print(lista[i])'''

#sposób 3
'''for i in lista[1::2]:#[45, 101, -5 , 7]
    print(i)'''

#sposób 4
'''i = 1
while i < len(lista):
    print(lista[i])
    i = i + 2'''
    # i += 1

#Zadanie 3.
'''lista = ['matematyka', 'fizyka', 'informatyka', 'język polski', 'język angielski']
for i in range(len(lista)):
    print(i)'''

'''lista = ['matematyka', 'fizyka', 'informatyka', 'język polski', 'język angielski'] 
for i in range(len(lista)): 
    print(lista[i])'''

#Zadanie 4.
lista3 = [67]
for x in lista3:
    liczba = float(input('Podaj liczbę'))
    print(liczba)
    if liczba != 0:
        lista3.append([])