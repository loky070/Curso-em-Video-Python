from time import sleep

def linha(tam=42):
    return '\033[1;35m=\033[m' * tam

def cabeçalho(txt):
    print(linha())
    print(f'\033[1;34m{txt.center(42)}\033[m')
    print(linha())

def leiaInt(inteiro):

    while True:
        try:
            numero = int(input(inteiro))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            sleep(1)
            continue
        # continue volta pro while True
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número\033[m')
            return 3

        else:
            return numero

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    contador = 1
    for i in lista:
        print(f'\033[34m{contador} -\033[m {i}')
        contador +=1
    print(linha())

    opc = leiaInt('Sua Opção: ')
    return opc