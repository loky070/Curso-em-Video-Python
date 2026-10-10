#tinha mt coisa em codigo ent achei melhor fzr um arquivo .py pra ajudar na prática

lanche = ('Arroz','Batata','Suco','Pudim')
numeros = (7,2,4,1,8,9,6,0,3,5)

#várias formas de mostrar tudo na lista
for comida in lanche:
    print(comida)
#chique
for contador in range(0,len(lanche)):
    print(lanche[contador])
#com isso dá pra enumerar
for posicao, comida in enumerate(lanche):
    print(f'{posicao} - {comida}')

#mostrando em ordem(não muda a ordem, apenas mostra)
print(sorted(lanche))
print(sorted(numeros))

a = (4,2,6)
b = (8,6,9,3)
c = a + b
print(c)

#conta o que tá nos ()
print(c.count(9))

#mostra a posição index, pega apenas a primeira ocorrência
print(c.index(6))

#dar pra escolher de quando começa
#vai procurar "6" a partir do 3° index
print(c.index(6,3))

#única forma de editar uma Tupla, é apagando ela por completo
pessoa = ('Dudu',19,'M',1.87)
del(pessoa)
#não dá pra fazer que nem em listas
'''a = [1,2,3]
del[a[1]]
print(a)'''