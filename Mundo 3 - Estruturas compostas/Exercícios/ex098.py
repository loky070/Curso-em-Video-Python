from time import sleep
def contagem(inicio,fim,passos):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f"{"="*40}")
    print(f"Contagem de {inicio} até {fim} de {passos} em {passos}")
    sleep(2.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ",end="", flush=True)
            sleep(0.5)
            cont += passos
        print("FIM")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ",end="", flush=True)
            sleep(0.5)
            cont -= passos
        print("FIM")

contagem(0,100,10)
contagem(10,0,2)
print("Agora é a sua vez de fazer!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contagem(ini,fim,passo)