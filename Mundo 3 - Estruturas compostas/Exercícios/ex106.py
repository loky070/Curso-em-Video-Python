from time import sleep

cores = (
    '\033[m',           # 0 - sem cores
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30m',       # 6 - branco
)

def linhas(palavra,cor):
    tamanho = len(palavra) + 4

    print(cores[cor],end='')
    print(f'{"="*tamanho}')
    print(f'{palavra:^{tamanho}}')
    print(f'{"="*tamanho}')
    print(cores[0],end='')

def ajuda(comando):

    linhas(f'Acessando o manual do comando \'{comando}\'',3)
    sleep(1)
    print(cores[5],end='',flush=True)
    help(comando)
    print(cores[0],end='',flush=True)
    sleep(1)


while True:
    linhas('SISTEMA DE AJUDA PyHELP',4)

    print(cores[0])
    opcao = str(input('Função ou Biblioteca > ')).lower().strip()
    if opcao == 'fim':
        linhas('ATÉ LOGO!',1)
        break

    ajuda(opcao)