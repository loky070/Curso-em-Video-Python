def area(l,c):
    a = l * c
    print(f"A área de um terreno {l}x{c} é de {a}m².")

print(f"{"Controle de terrenos":^25}\n{"="* 25}")
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura,comprimento)