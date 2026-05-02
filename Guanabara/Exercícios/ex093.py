dados = dict()
gols = list()
dados['Nome'] = str(input('Nome do jogador: '))
Partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? ' ))
print('='*40)
for x in range(Partidas):
    gols.append(int(input(f'    Quantos gols {dados["Nome"]} marcou na partida {x}? ')))
dados['Gols'] = gols[:]
dados['Total'] = sum(gols)
print('='*40)
for keys, values in dados.items():
    print(f'O campo {keys} tem o valor {values}')
print('='*40)
print(f'O jogador {dados["Nome"]} jogou {Partidas} partidas')
# FORMA GUANABAS
for i, v in enumerate(dados["Gols"]):
    print(f'    =>Na partida {i}, fez {v} gols.')
    
print(f'Foi um total de {dados["Total"]} gols')
'''--MINHA FORMA
for x in range(Partidas):
    # print(f'    => Na partida {x}, fez {gols[x]}')
    print(f'    => Na partida {x}, fez {dados["Gols"][x]}')'''