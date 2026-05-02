#forma rapida de criar uma TUPLA
num = tuple(int(input('Digite um número: '))for x in range(4))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram ',end='')
for x in num:
    if x % 2 == 0:
        print(x,end=' ')