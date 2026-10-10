print(f'{"LOOOOOUJA":-^40}')
total = caro = contador = barato = 0
item_barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
#aqui tamo adicionando o preço do produto
#no total
    total += preco
    contador += 1
#adicionando um item no contador de mais de 1k
    if preco > 1000:
        caro += 1
#se for a primeira vez q tá rodando
#o item mais barato vai ser o primeiro
#se não, ele vai checar se o item atual
#é mais barato ou não
    if contador == 1 or preco < barato:
        barato = preco
        item_barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''
O total da compra foi R${total:.2f}
Temos {caro} produtos custando mais de R$1000.00
O produto mais barato foi {item_barato} que custa R${barato:.2f}
''')