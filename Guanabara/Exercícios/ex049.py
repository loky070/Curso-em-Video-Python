numero = int(input('Digite um número para ver sua tabuada: '))
print('='*20)
for x in range(1,11):
    print(f'{numero} x {x:2} = {numero * x}')
print('='*20)