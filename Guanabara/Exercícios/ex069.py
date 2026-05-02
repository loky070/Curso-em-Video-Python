print(f'{"-"*20}\nCADASTRE UMA PESSOA\n{"-"*20}')
total_18 = total_mulheres20 = total_homens = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        total_18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            total_homens += 1
        if sexo == 'F' and idade < 20:
            total_mulheres20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''
Tem {total_18} pessoas com mais de 18 anos
Tem {total_homens} homens cadastrados
Tem {total_mulheres20} mulheres com menos de 20 anos
''')

