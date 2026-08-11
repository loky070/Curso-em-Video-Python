def leiaInt(inteiro):

    while True:
        try:
            numero = int(input(inteiro))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        # continue volta pro while True
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0

        else:
            return numero

def leiaFloat(real):
    while True:
        try:
            numero = float(input(real))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return numero

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor Inteiro digitado foi {n1} e o valor Real foi {n2}')
        