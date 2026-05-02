dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])

# print(dados[0]) não funciona
print(f'O {dados["nome"]} tem {dados["idade"]} anos')

dados['sexo'] = 'M'

del dados['idade']


filme = {
    'título': 'Star Wars', 
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme.values()) # retorna todos os VALORES (Star Wars, 1977, George Lucas)

for v in filme.values():
    print(v)


print(filme.keys()) # retorna todas as CHAVES(título, ano, diretor)

for k in filme.keys():
    print(k)

print(filme.items()) # retorna tudo

#seria entre muitas """" o enumerate do dicionário
for keys, values in filme.items():
    print(f'O {keys} é {values}')

locadora = list()
locadora.append(filme)
print(locadora)

brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['uf'])

estado = dict()
brasil = list()
for x in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
        print(f'{v}',end=' ')
    print()