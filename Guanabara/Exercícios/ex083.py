'''Minha resposta n funfou 100% pq pode abrir com ) e fechar com (
que conta como certo

lista_comeco = []
lista_fim = []
expre = str(input('Digite a expressão: '))
for x in expre:
    if x == '(':
        lista_comeco.append('(')
    if x == ')':
        lista_fim.append(')')

if len(lista_comeco) == len(lista_fim):
    print('Tudo certo')
else:
    print('Sua expressão está errada')'''

# Guanaba's Version
expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')

    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está ERRADA')