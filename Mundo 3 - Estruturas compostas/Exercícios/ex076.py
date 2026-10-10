print(f'{'-'*40}\n{'LISTA DE PRODUTOS':^40}\n{'-'*40}')
listagem = (
    "Lápis", 1.75,
    "Borracha", 2.00,
    "Caderno", 15.90,
    "Estojo", 25.00,
    "Transferidor", 4.20,
    "Compasso", 9.99,
    "Mochila", 120.32,
    "Canetas", 22.30,
    "Livro", 34.90
)
y = 0
for x in range(len(listagem)//2):
    print(f'{listagem[x + y]:.<31}R${listagem[x + y + 1]:>7.2f}')
    y += 1
print('-'*40)

#f"{valor:caractere_preenchimento_alinhamento_largura}"