nota1 = float(input('\033[33mDigite a primeira nota: \033[m'))
nota2 = float(input('\033[36mDigite a segunda nota: \033[m'))
media = (nota1+nota2)/2
print(f'Tirando \033[33m{nota1}\033[m e \033[36m{nota2}\033[m, a média do aluno é {media}')
if media < 5:
    print('\033[31mO aluno foi REPROVADO\033[m')
elif 5<=media<7:
    print('\033[33mO aluno está em RECUPERAÇÃO\033[m')
elif media >= 7:
    print('\033[329mO aluno foi APROVADO\033[m')