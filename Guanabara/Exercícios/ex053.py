frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    print(junto[letra])
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('\033[32mTemos um palíndromo\033[m')
else:
    print('\033[31mNão temos um palíndromo\033[m')

    
'''---Versão Menor---
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('\033[32mTemos um palíndromo\033[m')
else:
    print('\033[31mNão temos um palíndromo\033[m')
'''