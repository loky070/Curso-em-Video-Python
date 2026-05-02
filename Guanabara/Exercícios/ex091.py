from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),}

ranking = list()

print(f'{'VALORES SORTEADOS':=^40}')
for keys, values in jogo.items():
    print(f'O {keys} tirou {values}')
    sleep(1)

print(f'{'RANKING DOS JOGADORES':=^40}')
# coloca na variável RANKING uma lista de tuplas ordenadas pelo valor do índice que tiver no key=itemgetter()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) 

for i, v in enumerate(ranking):
                            #.center(padding) vai vir dps que vc fecha as 'ASPAS' e centraliza tudo na margem colocada
    print(f'{i+1}° lugar: {v[0]}'.center(40))
    sleep(1)