soma_idade = 0
mulheres_novas = 0
maior_idade = 0
nome_homem = ''
for x in range(1,5):
    print(f'--- {x}° PESSOA ---')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()

    soma_idade += idade

    if sexo == 'F' and idade < 20:
        mulheres_novas += 1

    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_homem = nome

media_idade = soma_idade/4

print(f'''
A média de idade é {media_idade}
O homem com maior idade tem {maior_idade} anos e se chama {nome_homem}
Tem {mulheres_novas} mulheres com menos de 20 anos
''')