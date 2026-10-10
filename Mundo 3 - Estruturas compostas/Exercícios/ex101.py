
# def voto(nascimento):

#     from datetime import datetime

#     ano_atual = datetime.now().year
#     # se tu importa dentro da função, ela só funciona dentro da função

#     idade = ano_atual - nascimento

#     if idade < 18:
#         print(f'Com {idade} anos: NÃO VOTA')
#     elif 18 <= idade <65:
#         print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
#     else:
#         print(f'Com {idade} anos: VOTO OPCIONAL')

# fiz meio errado.
# forma do Guanabara:

def voto(ano):

    from datetime import date
    atual = date.today().year
    # se tu importa dentro da função, ela só funciona dentro da função (Escopo de Importação)

    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

nasc = int(input('Digite seu ano de nascimento: '))

print(voto(nasc))