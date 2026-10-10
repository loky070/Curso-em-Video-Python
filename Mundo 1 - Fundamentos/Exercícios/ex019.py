from random import choice

lista = []

for x in range(4):
    nome = input(f'Digite o {x+1}° nome: ')
    lista.append(nome)

sorteado = choice(lista)
print(f'O sorteado foi {sorteado}.')
