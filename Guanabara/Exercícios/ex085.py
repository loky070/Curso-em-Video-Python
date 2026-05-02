lista = [[],[]]
for x in range(7):
    numero = int(input(f'Digite o {x+1}° valor: '))
    if numero % 2 == 0:
        lista[0].insert(0,numero)
    else:
        lista[1].insert(1,numero)

lista[0].sort()
lista[1].sort()
print(f'Os valores pares foram: {lista[0]}')
print(f'Os valores ímpares foram: {lista[1]}')