dados = list()
dados.append('Pedro')
dados.append(25)

pessoa = list()
# Ele cria uma cópia
pessoa.append(dados[:])
# e vai ficar os dados de Nome e data em um index
print(pessoa[0])


# agora no plural kkkk
pessoas = [['Pedro',25],['Maria',19],['João',32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])


# Fazendo assim, vai ficar duas vezes Maria 22 na lista, pq as listas estão conectadas
teste = list()
teste.append('Gustavo')
teste.append('40')

galera = list()
galera.append(teste)
print(galera)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)

print(galera)

# /////////////////////////////////

teste = list() #aki a gente criou uma lista com Gustavo, 40
teste.append('Gustavo')
teste.append('40')

galera = list()
galera.append(teste[:]) # aki a gente atribuiu os valores que tinha na lista "teste",  pra lista "galera"
print(galera)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #depois alteramos os valores da lista "teste" pra adicionar de novo na lista "galera"
# se não colocarmos o [:], ele vai criar uma ligação entre as duas listas e vai printar "Maria" "22" duas vezes
print(galera)

galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')



# sistema simples 

galera = list()
dado = list()
totmaior = totmenor = 0
for p in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: '))) #coloco o nome e idade dentro de uma lista
    galera.append(dado[:]) #coloco uma CÓPIA dessa lista dentro da outra lista galera
    dado.clear() #limpo a lista "dado"
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')