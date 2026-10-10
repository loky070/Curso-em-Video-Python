from random import choice

numeros = [0,1,2,3,4,5]
sorteado = choice(numeros)

for x in range(3):
    tentativa = int(input('Tente adivinhar o número que estou pensando de 0 a 5: '))
    if tentativa == sorteado:
        print('\033[32mParabéns! Você adivinhou!!!\033[m')
        break

    else:
        print('\033[31mVocê errou!\033[m')
print(f'O número era {sorteado}')