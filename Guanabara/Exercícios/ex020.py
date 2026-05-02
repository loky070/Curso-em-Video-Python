from random import shuffle

lista = []

for x in range (4):
    nomes = input(f'Digite o {x+1}° aluno: ')
    lista.append(nomes)

shuffle(lista)

print(f'A ordem de apresentação é: \n{lista}')