sair = False
numero1 = int(input('PRIMEIRO VALOR: '))
numero2 = int(input('SEGUNDO VALOR: '))

while sair == False:
    print('=-'*15)
    print('''
[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA
''')
    escolha = int(input('>>>>>DIGITE A OPÇÃO: '))
    print('=-'*15)
    if escolha == 1:
        soma = numero1 + numero2
        print(f'A soma de {numero1} e {numero2} é {soma}.')
        
    elif escolha == 2:
        multi = numero1 * numero2
        print(f'A multiplicação de {numero1} e {numero2} é {multi}.')
        
    elif escolha == 3:
        if numero1 > numero2:
            print(f'O número {numero1} é maior que o número {numero2}.')
        elif numero2 > numero1:
            print(f'O número {numero2} é maior que o número {numero1}.')
        elif numero1 == numero2:
            print('Os dois números são iguais.')
    elif escolha == 4:
        numero1 = int(input('Digite o novo 1° número: '))
        numero2 = int(input('Digite o novo 2° número: '))
    elif escolha == 5:
        print('>>>>>Até logo!')
        sair = True