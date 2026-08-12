from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('EXISTE')
else:
    print('NÃO EXISTE')

while True:
    resposta = menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1 :
        cabeçalho('opção 1')

    elif resposta == 2:
        cabeçalho('opção 2')

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO: por favor, digite uma opção válida.')
        sleep(1)
    
