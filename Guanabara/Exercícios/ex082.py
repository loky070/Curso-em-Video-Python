'''lista = []
lista_par = []
lista_impar = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if escolha in 'N':
        break
for x in lista:
    if x % 2 == 0:
        lista_par.append(x)
    else:
        lista_impar.append(x)
print(f'''
'''A lista completa é {lista}
A lista de pares é {lista_par}
A lista de ímpares é {lista_impar}'''
''')'''

#Guanaba's Version
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'''
A lista completa é {num}
A lista de pares é {pares}
A lista de ímpares é {impares}
''')