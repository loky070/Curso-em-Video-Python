soma = 0
contador = 0
while True:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        contador += 1
    else:
        break
print(f'A soma dos {contador} valores foi {soma}.')
    