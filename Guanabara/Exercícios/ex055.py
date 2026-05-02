'''---Minha Versão---
lista = []
for x in range(1,6):
    peso = float(input(f'Peso da {x}° pessoa: '))
    lista.append(peso)
maior = max(lista)
menor = min(lista)
print(f'O maior peso da lista é {maior}Kg\nO menor peso da lista é {menor}Kg')'''


'''---Versão Guanabara---(gostei da lógica usada aqui)'''

maior = 0
menor = 0
for x in range(1,6):
    peso = float(input(f'Digite o peso da {x}° pessoa: '))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}Kg\nO menor peso foi {menor}Kg')