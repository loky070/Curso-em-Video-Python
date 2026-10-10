from datetime import date

ano = int(input('Digite o ano(coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[32mO ano {ano} é Bissexto\033[m')
else:
    print(f'\033[31mO ano {ano} não é Bissexto\033[m')