def linha():
    print("="*30)

def contador(*num):
    linha()
    print(f"Analisando os valores passados...")
    cont = maior = 0
    for x in num:
        if cont == 0:
            maior = x
        else:
            if x > maior:
                maior = x
        cont += 1
        print(f"{x} ",end="", flush=True)
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {maior}")

contador(2, 9, 4, 5, 7, 1)
contador(4, 7, 0)
contador(1, 2)
contador(6)
contador(-3,-5,-7)
contador()