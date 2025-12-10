#Tabliczka mnożenia
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end = '\t')
        #print(f'{i} * {j} = {i * j}')
    # print()

#Trójkąt prostokątny
# n = int(input('Wysokość trójkąta = '))
# for x in range(n):
#     for y in range(x + 1):
#         print('*', end = '')
#     print()

# n = int(input('Wysokość trójkąta = '))
# for x in range(n):
#     print('*' * (x + 1))

#Trójkąt równomierny dowolny
n = int(input('Wysokość trójkąta = '))
spacje = n - 1
gwiazdki = 1

for i in range(n):
    print(' ' * spacje, end = '')
    print('*' * gwiazdki)
    spacje = spacje - 1
    gwiazdki = gwiazdki + 2