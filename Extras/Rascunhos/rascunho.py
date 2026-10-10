from random import randint
from time import sleep

lista_de_jogos = []
dados = []

print('-' * 35)
print(f'{"JOGADOR DE MEGA-SENA":^35}')
print('-' * 35)

quantidade = int(input('Quantos jogos quer que eu sorteie? '))

while len(lista_de_jogos) < quantidade:
    # Gera um jogo de 6 números (Mega-Sena)
    while len(dados) < 15:
        numero = randint(1, 25)
        if numero not in dados:
            dados.append(numero)
    
    dados.sort()
    
    # SÓ ADICIONA SE O JOGO FOR NOVO (Evita jogos repetidos)
    if dados not in lista_de_jogos:
        lista_de_jogos.append(dados[:])
    
    dados.clear()

print(f'{f" SORTEANDO {quantidade} JOGOS ":=^35}')
for i, jogo in enumerate(lista_de_jogos):
    print(f'Jogo {i+1}: {jogo}')
    sleep(0.3)

print(f'{" < BOA SORTE! > ":=^35}')