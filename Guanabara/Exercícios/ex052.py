numero = int(input('Digite o número: '))
quantidade = 0
for x in range(1,numero + 1):
    if numero % x == 0:
        print(f'\033[31m{x}\033[m', end=(' '))
        quantidade +=1
    else:
        print(f'\033[33m{x}\033[m', end=(' '))

print(f'\nO número {numero} foi divisível {quantidade} vezes')

if quantidade == 2:
    print('Por isso ele \033[32mÉ PRIMO\033[m') 
else:
    print('Por isso ele \033[31mNÃO É PRIMO\033[m')