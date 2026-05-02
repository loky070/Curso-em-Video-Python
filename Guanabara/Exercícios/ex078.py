# até funciona mas so mostra 1 vez o número
# lista = []
# for x in range(5):
#     lista.append(int(input(f'Digite o valor para a posição {x}: ')))
# print(f'O maior valor na posição {lista.index(max(lista))} foi o número {max(lista)}')
# print(f'O menor valor na posição {lista.index(min(lista))} foi o número {min(lista)}')

# Guanabara's Version
lista = []
maior = menor = 0
for x in range(5):
    lista.append(int(input(f'Digite o valor para a posição {x}: ')))
    if x == 0:
        maior = menor = lista[x]
    else:
        if lista[x] > maior:
            maior = lista[x]

        if lista[x] < menor:
            menor = lista[x]

print(lista)

print(f'O maior valor foi o número {max(lista)} nas posições: ',end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice}...',end='')
print()
print(f'O menor valor foi o número {min(lista)} nas posições: ',end='')
for indice, valor in enumerate(lista):
    if valor == menor:  
        print(f'{indice}...',end='')