salario = float(input('Digite seu \033[32msalário\033[m para receber um aumento:\033[32m \033[m'))
if salario > 1250:
    novo = salario * 1.1
    print(f'você ganhou um aumento de \033[32m10%\033[m. O seu novo salário é de R${novo:.2f}.')
else:
    novo = salario * 1.15
    print(f'você ganhou um aumento de \033[32m15%\033[m. O seu novo salário é de R${novo:.2f}.')