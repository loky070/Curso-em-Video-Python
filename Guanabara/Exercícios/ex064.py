'''---MINHA VERSÃO
total = c = a = 0
while a != 999:
    a = int(input('Digite o número [999 para parar]: '))
    if a != 999:
        c += 1
        total += a 
print(f'Soma total: {total}\nQuantidades de Inputs:{c}')
'''

'''GUANABA'S VERSION(ficou melhor)''' 
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]'))
print(f'Soma total: {soma}\nQuantidades de Inputs:{cont}')