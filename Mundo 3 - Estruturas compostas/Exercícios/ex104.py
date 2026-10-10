def leiaInt(mensagem):

    certo = False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            certo = True
        else:
            print('\033[31mErro! Digite um número inteiro válido\033[m')
        if certo:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')