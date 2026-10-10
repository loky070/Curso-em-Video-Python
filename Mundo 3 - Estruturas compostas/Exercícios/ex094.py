pessoas = list()
dados_pessoa = dict()

soma = 0
while True:

    dados_pessoa["Nome"] = str(input('Nome: ')).strip().capitalize() #.title() Deixa a Primeira Letra De Cada Palavra Em Maiúscula
    while True:
        dados_pessoa["Sexo"] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados_pessoa['Sexo'] in 'MF':
            break
        print('Favor, digite apenas M ou F.')
    dados_pessoa["Idade"] = int(input('Idade: '))
    
    soma += dados_pessoa["Idade"]

    # [:] copia LISTASSSSS, .copy() copia DICIONÁRIOSSSS
    pessoas.append(dados_pessoa.copy())

    while True:
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('Responda apenas S ou N')
    if escolha == 'S':
        break

media_idade = soma / len(pessoas)

print(f'''
- O grupo tem {len(pessoas)} pessoas
- A média de idade é de {media_idade:5.2f}
- As mulheres cadastradas foram: ''',end='')
for p in pessoas:
    if p["Sexo"] == 'F':
        print(p["Nome"],end='; ')

print(f'\n- Lista de pessoas acima da média:')
for p in pessoas:
    if p["Idade"] >= media_idade:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('\n<<<ENCERRADO>>>')