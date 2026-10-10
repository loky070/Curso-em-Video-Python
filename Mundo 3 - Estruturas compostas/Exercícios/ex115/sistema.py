from lib.interface import *
from lib.arquivo import *
from time import sleep
import os

arq = os.path.join(os.path.dirname(__file__), 'cursoemvideo.txt')

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1 :
        # opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('opção 2')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO: por favor, digite uma opção válida.')
        sleep(1)
    
