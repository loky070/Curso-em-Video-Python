from random import randint

def sorteia(lista):
    print("Sorteando 5 valores da lista: ",end="")
    for x in range(5):
        n = randint(1,10)
        lista.append(n)
        print(n,end=" ",flush=True)
    print("PRONTO!")

def somaPar(lista):
    soma = sum(x for x in lista if x % 2 == 0)
    print(f"Somando os valores pares de {lista}, temos {soma}")

numeros = list() 
sorteia(numeros)
somaPar(numeros)