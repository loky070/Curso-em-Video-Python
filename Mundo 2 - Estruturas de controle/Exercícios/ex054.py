maior = 0
menor = 0
for x in range(7):
    ano = int(input(f'{x+1}-Digite seu ano de Nascimento: '))
    if 2026 - ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já atingiram a maioridade e {menor} pessoas ainda NÃO atingiram.')

'''---Versão com datetime
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for x in range(1,8):
    ano = int(input(f'{x}-Digite seu ano de Nascimento: '))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já atingiram a maioridade e {menor} pessoas ainda NÃO atingiram.')
'''

'''---Guanaba's version
galera = list()
dado = list()
totmaior = totmenor = 0
for p in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: '))) #coloco o nome e idade dentro de uma lista
    galera.append(dado[:]) #coloco uma CÓPIA dessa lista dentro da outra lista galera
    dado.clear() #limpo a lista "dado"
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')


'''