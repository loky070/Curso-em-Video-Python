'''eu fiz assim
s = 0
for x in range(0,500,3):
    if x % 2 != 0:
        s += x
print(s)'''

'''guanabas'''
soma = 0
cont = 0
for x in range(1,501,2):
    if x % 3 == 0:
        cont += 1
        soma += x
print(f'A soma dos {cont} números foram {soma}')