from random import randint
print(f'{"="*25}\nVAMOS JOGAR PAR OU ÍMPAR\n{"="*25}')
vitorias = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Digite seu número: ').strip())
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    soma = jogador + computador
    resultado = soma % 2
    print(f'{"="*25}')
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu {'PAR'if resultado == 0 else 'IMPAR'}')
    print(f'{"="*25}')
    if resultado == 0:
        if pi == 'P':
            print(f'\033[32mJOGADOR VENCE\033[m\nVamos de novo!\n{'='*25}')
            vitorias += 1 
        else:
            print('\033[31mCOMPUTADOR VENCE\033[m')
            break
    elif resultado == 1:
        if pi == 'I':
            print(f'\033[32mJOGADOR VENCE\033[m\nVamos de novo!\n{'='*25}')
            vitorias += 1 
        else:
            print('\033[31mCOMPUTADOR VENCE\033[m')
            break         
print(f'{"="*25}\n\033[1;31mGAME OVER!\033[m Você venceu \033[32m{vitorias}\033[m vezes.\n')
