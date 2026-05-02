primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite o número da razão: '))
limite = 10
while limite > 0:
    print(primeiro,end=' → ')
    primeiro += razao
    limite -=1
print('Terminou')