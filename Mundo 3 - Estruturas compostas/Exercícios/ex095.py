jogadores = list()
dados = dict()
gols = list()
codigo = 0
while True:
    dados["Código"] = codigo
    dados['Nome'] = str(input('Nome do jogador: ')).title()
    Partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? ' ))
    print('='*60)
    gols.clear()
    for x in range(Partidas):

        gols.append(int(input(f'    Quantos gols {dados["Nome"]} marcou na partida {x}? ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    print('='*60)
    jogadores.append(dados.copy())
    codigo += 1

    while True:
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('Responda apenas S ou N')
    if escolha == 'N':
        break
    
print('='*60)
print(f'{"COD":^6}{"NOME":^20}{"GOLS":^25}{"TOTAL":^8}')
print('-'*60)

for pessoa in jogadores:
    print(f'{pessoa["Código"]:^6}'
          f'{pessoa["Nome"]:^20}'
          f'{str(pessoa["Gols"]):^25}'
          f'{pessoa["Total"]:^8}')
print('='*60)
while True:

    escolha = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    print('='*60)
    if escolha == 999:
        break
    if escolha >= len(jogadores):
        print('ERRO! Não existe jogador com esse código.')
        continue
    
    print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[escolha]["Nome"]}')

    for i, v in enumerate(jogadores[escolha]["Gols"]):
        print(f'    => Na partida {i}, fez {v} gols.')
    print('='*60)