# preferi fzr outro arquivo pra não confundi
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).title()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? ' ))
    partidas.clear()
    print('='*40)
    for x in range(tot):
        partidas.append(int(input(f'    Quantos gols {jogador["Nome"]} marcou na partida {x+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('Responda apenas S ou N')
    if escolha == 'N':
        break
print('='*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40) 
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i + 1}, fez {g} gols.')
    print('-'*40) 
print('<< VOLTE SEMPRE >>')
