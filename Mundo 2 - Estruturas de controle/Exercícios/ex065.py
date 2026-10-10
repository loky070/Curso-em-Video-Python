resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}.')
print(f'O maior número foi {maior}.\nO menor número foi {menor}.')

'''>>>>>versão refeita do 0 pra ver se fixou
resp = 'S'
soma = maior = menor = cont = 0
while resp in 'S':
    cont +=1
    num = int(input('Digite o número: '))
    resp = str(input('Você gostaria de continuar? [S/N]: ')).upper().strip()[0]
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
            
media = soma / cont
print(f'''
'''A média dos {cont} números digitados foram {media}
O maior número foi {maior}
O menor número foi {menor}'''
''')'''