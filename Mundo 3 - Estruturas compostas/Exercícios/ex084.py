lista = []
#vou detalhar bem esse pra não esquecer

dados = []  #criamos a lista
menor = maior = 0   #criamos as variáveis de > e <
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: '))) #colocar nome e peso
    if len(lista) == 0: #se não tiver nada na lista principal(ainda não adicionamos "dados" na "lista")
        maior = menor = dados[1]    #maior e menor vão ser o índice 1 que no caso é peso
    else:   #se não
        if dados[1] > maior:    #se o peso for maior do que o que estava cadastrado antes
            maior = dados[1]    #ele vira o novo maior peso
        if dados[1] < menor:    #se o peso for menor do que o que estava cadastrado antes
            menor = dados[1]    #ele vira o novo menor peso
            
    lista.append(dados[:])  #depois de fzr a verificação de peso, fazemos uma cópia de "dados" pra "lista" 
    dados.clear()   #e limpamos a lista "dados"
    
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()  #pergunta se quer continuar
    print('='*30)
    if resp in 'NNAONÃO':   #se for não
        break   #ele sai

print(f'Você cadastrou {len(lista)} pessoas')   #mostra a quantidade de pessoas
#como cada pessoa está dentro de uma lista, conta como 1, 
#ai não tem aquilo de nome e numero contarem como 2 seres para o len, e sim contam como apenas 1

print(f'O maior peso foi de {maior}Kg. Peso de ',end='')    #mostra o maior peso
for p in lista: #vai rodar a lista
    if p[1] == maior:   #se o indice 1(o peso) for igual ao do maior
        print(f'[{p[0]}] ',end='')  #ele vai printar o nome da pessoa
        
print(f'\nO menor peso foi de {menor}Kg. Peso de ',end='')  #mesma coisa do de cima
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]',end='')