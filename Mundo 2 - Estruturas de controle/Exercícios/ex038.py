num1 = int(input('\033[31mDigite o primeiro número: \033[m'))
num2 = int(input('\033[34mDigite o segundo número: \033[m'))
if num1 > num2:
    print('O \033[31mprimeiro valor\033[m é maior que o segundo valor.')
elif num2 > num1:
    print('O \033[34msegundo valor\033[m é maior que o primeiro valor.')
else:
    print('\033[35mOs dois números são iguais.\033[m')