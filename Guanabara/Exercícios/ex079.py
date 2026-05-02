lista = []
while True:
    print('='*35)
    numero = int(input('Digite um valor: '))
    if numero in lista:
        print('Valor duplicado não será adicionado')
    else:
        lista.append(numero)
        print('Valor adicionado com sucesso...')
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
lista.sort()
print('='*35)
print(f'Você digitou os valores {lista}')