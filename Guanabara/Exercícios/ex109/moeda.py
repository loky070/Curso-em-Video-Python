def metade(preço=0, format=False):
    '''
    
    '''
    resultado = preço / 2 
    return resultado if format is False else moeda(resultado)

def dobro(preço=0, format=False):
    resultado = preço * 2
    return resultado if format is False else moeda(resultado)

def aumentar(preço=0, taxa=0, format=False):
    resultado = preço + (preço * taxa / 100)

    return resultado if not format else moeda(resultado) 
    # outra forma de fzr 

def reduzir(preço=0, taxa=0, format=False):
    resultado = preço - (preço * taxa / 100)
    return resultado if format is False else moeda(resultado)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')