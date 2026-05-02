nome = input('Digite seu nome: ')
print(f'''
Nome em maiúsculas: {nome.upper()}
Nome em minúsculas: {nome.lower()}
Nome sem espaços: {len(nome.replace(' ',''))} letras
Primeiro nome tem {len(nome.split()[0])} letras''')