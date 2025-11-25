lista = [10, 56, 89, 59]
#1 Chodzenie bezpośrednio po elementach listy
# Do zmiennej b trafiają bezpośrednio elementy listy tzn. 10, 56, 89, 59
'''for b in lista:
    print(b)'''

#2 Chodzenie po liście z użyciem indeksów
#2.1 Co to jest indeks?
# lista[2]
# 2 - indeks
#lista[2] - element znajdujący się pod indeksem 2 = 89

#2.2.
for k in range(len(lista)): #range(0, 4)
    print(lista[k])
