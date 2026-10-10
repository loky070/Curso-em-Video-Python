import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p, "US$")} é {moeda.moeda(moeda.metade(p))}')
# deixei em dolar só pra saber que dá pra fzr isso
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.reduzir(p,13))}')