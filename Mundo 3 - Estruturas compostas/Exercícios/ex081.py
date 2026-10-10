'''lista = []
contador = 0
while True:
    numero = int(input('Digite um valor: '))
    contador += 1
    lista.append(numero)
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if escolha in 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {contador} números.')
print(f'Os números em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado.')'''

'''---Guanaba's Version'''
valores = []
while True:
    valores.append(int(input('Digite os valores: '))) #Forma mais fácil de add numa lista com input os valores 
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('='*30)
valores.sort(reverse=True)
print(f'''
Você digitou {len(valores)} elementos.
Os valores em ordem decrescente são {valores}''')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado.')