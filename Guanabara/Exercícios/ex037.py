num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print(f'{opcao} convertido em BINÁRIO é {bin(num)}')
elif opcao == 2:
    print(f'{opcao} convertido em OCTAL é {oct(num)}')
elif opcao == 3:
    print(f'{opcao} convertido em HEXA é {hex(num)}')