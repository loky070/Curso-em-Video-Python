lista = []
for c in range(5):
    numero = int(input('Digite o valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado na última posição da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos,numero)
                print(f'Adicionado na posição {pos}')
                break
            pos +=1
print('='*30)
print(f'Os valores digitados foram: {lista}')
