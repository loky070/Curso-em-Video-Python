from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual sua jogada? '))
if jogador not in (0, 1, 2):
    print('\033[1;31mJOGADA INVÁLIDA\033[m')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!!')
    print('\033[47m=\033[m' * 20)
    print(f'''Computador: {itens[computador]}
    jogador: {itens[jogador]}''')
    print('\033[47m=\033[m' * 20)

    if computador == 0: #PEDRA
        if jogador == 0:
            print('\033[36mEMPATE\033[m')
        elif jogador == 1:
            print('\033[32mJOGADOR VENCE\033[m')
        elif jogador == 2:
            print('\033[31mCOMPUTADOR VENCE\033[m')

    elif computador == 1:
        if jogador == 0:
            print('\033[31mCOMPUTADOR VENCE\033[m')
        elif jogador == 1:
            print('\033[36mEMPATE\033[m')
        elif jogador == 2:
            print('\033[32mJOGADOR VENCE\033[m')

    elif computador == 2:
        if jogador == 0:
            print('\033[32mJOGADOR VENCE\033[m')
        elif jogador == 1:
            print('\033[31mCOMPUTADOR VENCE\033[m')
        elif jogador == 2:
            print('\033[36mEMPATE\033[m')
