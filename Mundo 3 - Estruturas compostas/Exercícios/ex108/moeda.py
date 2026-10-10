def metade(p):
    return p / 2

def dobro(p):
    return p * 2

def aumentar(p, n):
    return p + (p * n / 100)

def reduzir(p, n):
    return p - (p * n / 100)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')