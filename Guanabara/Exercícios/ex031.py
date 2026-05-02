viagem = float(input('Digite os quilômetros da viagem: '))
if viagem <= 200:
    valor = viagem * 0.5
    print(f'A viagem foi até 200Km, então cobraremos R$0,50 por Km, sendo o valor total de R${valor:.2f}')
else:
    valor = viagem * 0.45
    print(f'A viagem foi mais de 200Km, então cobraremos R$0,45 por Km, sendo o valor total de R${valor:.2f}')