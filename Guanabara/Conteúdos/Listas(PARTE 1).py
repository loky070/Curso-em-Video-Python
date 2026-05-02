lista = []
lista.append(3)
lista.append(4)
lista.append(5)

# for cont in range(5):
#     lista.append(int(input('Digite um valor: ')))
# print(lista)

# enumerate funciona igual aki
for pos, valor in enumerate(lista):
    print(f'Na posição {pos}, encontrei o valor {valor}.')
print('ACABOU')


# fato SUPER importante aqui
a = [1,2,3,4,5]
# se vc faz isso:
b = a
# você cria uma ligação entre as listas, e oq muda em uma muda em outra
# ex:
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#pra copiar de uma lista pra outra, tem que ser assim:
c = [1,2,3,4,5]
d = c[:]
d[2] = 8 
print(f'Lista C: {c}')
print(f'Lista D: {d}')