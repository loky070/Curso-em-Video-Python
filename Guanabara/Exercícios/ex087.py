matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior = terceira = soma = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))

print('='*30)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
    print()
print('='*30)
print(f'A soma de todos os valores pares é {soma}.')

for linha in range(3):
    terceira += matriz[linha][2]
print(f'A soma de todos os valores da 3° coluna é {terceira}.')

for coluna in range(3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da 2° linha é {maior}.')