from datetime import datetime
ano_atual = datetime.now().year
dados = dict()

dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = ano_atual - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Contratação'] - nasc + 35
print('='*30)
for keys, items in dados.items():
    print(f'    - {keys} tem o valor {items}')
