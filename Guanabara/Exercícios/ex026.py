frase = input('Digite uma frase: ').strip()

print(f'''
A letra 'A' aparece {frase.upper().count('A')} vezes.
A letra 'A' aparece pela primeira vez na posição {frase.upper().find('A') + 1}
A letra 'A' aparece pela primeira vez na posição {frase.upper().rfind('A') + 1}
''')