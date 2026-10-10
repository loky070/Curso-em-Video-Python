palavras = ('aprender','programar','estudar','hard','intenso','continue','melhore','mais')
for i in palavras:
    print(f'\nNa palavra {i.upper()}, temos: ',end=' ')
    for letra in i:
        if letra in 'aeiou':
            print(letra,end=' ')
    