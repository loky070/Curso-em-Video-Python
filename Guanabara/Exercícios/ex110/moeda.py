def metade(preço = 0, format = False):

    resultado = preço / 2 
    return resultado if format is False else moeda(resultado)

def dobro(preço = 0, format = False):
    resultado = preço * 2
    return resultado if format is False else moeda(resultado)

def aumentar(preço = 0, taxa = 0, format = False):
    resultado = preço + (preço * taxa / 100)

    return resultado if not format else moeda(resultado) 
    # outra forma de fzr 

def reduzir(preço = 0, taxa = 0, format = False):
    resultado = preço - (preço * taxa / 100)
    return resultado if format is False else moeda(resultado)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço = 0, percmais = 10, percmenos = 5):
    print(f'''
{'RESUMO DO VALOR':=^35}
Preço analisado: \t{moeda(preço)}
Dobro do preço: \t{dobro(preço,True)}
Metade do preço: \t{metade(preço,True)}
{percmais}% de aumento: \t{aumentar(preço,percmais,True)}
{percmenos}% de redução: \t{reduzir(preço,percmenos,True)}
{'=' * 35}
''')

