def ficha(nome='desconhecido',gols = 0):

    print(f'{'='*30}')
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

jogador = str(input('Nome do jogador: ')).strip()
gols = str(input('Números de gols: ').strip())

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if jogador == '':
    ficha(gols=gols) 
else:
    ficha(jogador,gols)

