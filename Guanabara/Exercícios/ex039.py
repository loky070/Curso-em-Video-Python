#eu fiz outra versão sem date.time mas achei melhor deixar essa msm

from datetime import date
atual = date.today().year
print('\033[7m='* 40)
nasc = int(input('\033[mDigite seu ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('\033[32mVocê tem que se alistar \033[4mIMEDIATAMENTE\033[m')
elif idade < 18:
    saldo = 18 - idade
    print(f'\033[34mAinda faltam \033[4m{saldo} anos\033[m \033[34mpara o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em \033[4m{ano}\033[m')
elif idade > 18:
    saldo = idade - 18
    print(f'\033[31mVocê já deveria ter se alistado há \033[4m{saldo} anos\033[m')
    ano = atual - saldo
    print(f'\033[31mSeu alistamento foi em \033[4m{ano}\033[m')
print('\033[7m='* 40)
print('\033[m')