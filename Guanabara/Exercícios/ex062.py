primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite o número da razão: '))
limite = 10
contador = 0
while limite > 0:
    print(primeiro,end='')
    print(end=' → ' if limite != 1 else ' → PAUSA ')
    primeiro += razao
    limite -=1
    contador += 1   
    if limite == 0:
        escolha = int(input('Deseja continuar com mais quantos termos?(Digite 0 se não: )'))
        if escolha != 0:
            limite = escolha
print(f'Progressão finalizada com {contador} termos mostrados.')

