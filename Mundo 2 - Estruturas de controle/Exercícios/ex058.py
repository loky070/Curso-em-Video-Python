'''
Dava pra fzr com choice,mas a forma do guanaba é menor.
from random import choice
lista = [1,2,3,4,5]
escolhido = choice(lista)
print(escolhido)
'''
from random import randint
tentativas = 0
computador= randint(0, 10)
jogador = None
print('Tente adivinhar o número que pensei de 0 a 10.')
while jogador != computador:
    jogador = int(input('Tente adivinhar: '))
    tentativas += 1
    if jogador > computador:
        print('Menos... Tente novamente.')
    elif jogador < computador:
        print('Mais... Tente novamente.')
print(f'Parabéns, você acertou com {tentativas} tentativas!')

'''guanaba's version foi usando booleano pra quando acertasse ficasse positivo
(o que imaginei sendo mais fácil), ai tentei fzr mais difícil'''