from random import randint

numeros = tuple(randint(1, 10) for _ in range(5))
#a outra opção era fzr essa coisa feia ai,quis nn
#numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados foram:',end=' ')
for i in numeros:
    print(f'{i}',end=' ')    
print(f'\nO maior valor foi {max(numeros)}')
print(f'O menor valor foi {min(numeros)}')