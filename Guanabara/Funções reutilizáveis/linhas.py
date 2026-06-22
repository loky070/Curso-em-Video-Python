def linhas(palavra):
    tamanho = len(palavra) + 4

    print("="*tamanho)
    print(f'{palavra:^{tamanho}}')
    print("="*tamanho)