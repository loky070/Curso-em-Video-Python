produto = float(input('Digite o preço do produto: R$'))
desconto = produto - (produto * 0.05)

print(f'O produto custa R${produto:.2f} reais, com 5% de desconto fica em R$ {desconto:.2f} reais.')
