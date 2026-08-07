import moeda
# ou só import moeda
# from moeda import metade,dobro,aumentar,reduzir

p = float(input('Digite o preço: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(p,13)}')