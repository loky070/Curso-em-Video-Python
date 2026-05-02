from random import randint
from time import sleep
lista = []
dados = []
while True:
    quantidade = int(input('Quantos jogos quer que eu sorteie? '))
    print(f'{f' SORTEANDO {quantidade} JOGOS ':=^35}')
    for x in range(quantidade):
        while len(dados) != 6:
            numero = randint(0,60)
            if numero not in dados:
                dados.append(numero)
        dados.sort()        
        lista.append(dados[:])
        dados.clear()
    break
for y,x in enumerate(lista):
    print(f'Jogo {y+1}: {x}',end='\n')
    sleep(1)
print(f'{'BOA SORTE':=^35}')
