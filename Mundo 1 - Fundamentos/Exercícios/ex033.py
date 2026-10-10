numeros = []
for x in range (3):
    num = int(input('Digite um numero: '))
    numeros.append(num)
print(f'''
O maior número da lista é {max(numeros)}
O menor número da lista é {min(numeros)}''')

#dava pra usar varios if e else tipo if a>b etxetx mas não gosto assim ent pesquisei mais fundo pra saber se tinha outra coisa que fazia a msm coisa de forma resumida, ai achei os max() e min()