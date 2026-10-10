primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite o número da razão: '))
decimo = primeiro + (10 - 1) * razao
for x in range(primeiro,decimo + razao ,razao):
    print(x,end=' → ')
print('Terminou')