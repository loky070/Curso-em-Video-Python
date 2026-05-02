valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Quantidade de anos de financiamento: '))
prestacao_mensal = valor_casa / (12 * anos)
limite_prestacao = salario * 0.3
print(f'Para pagar uma casa de {valor_casa:.0f} em {anos:.0f} anos, a prestação será de {prestacao_mensal:.2f}')
if prestacao_mensal > limite_prestacao:
    print('Empréstimo \033[31mNEGADO\033[m')
else:
    print('Empréstimo \033[32mCONCEDIDO\033[m')