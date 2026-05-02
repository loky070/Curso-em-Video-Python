km = float(input('Digite a quantidade de Km percorridos: '))
dias = float(input('Digite a quantidade de dias usados: '))

preco = (km * 0.15) + (dias * 60)

print(f'Tem que pagar R${preco}')