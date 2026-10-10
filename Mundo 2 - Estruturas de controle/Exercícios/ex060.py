numero = int(input('Digite o número: '))
contador = numero
f = 1
print(f'Calculando {numero}! = ', end='')
while contador > 0:
    print(f'{contador}', end = '')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print(f'{f}')

'''>>>>>COM FOR 
numero = int(input('Digite o número: '))
c = numero
f = 1
for x in range(1,c+1):
    f *= c
    c -= 1
print(f)'''