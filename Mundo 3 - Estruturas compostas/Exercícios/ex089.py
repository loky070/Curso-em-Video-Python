# alunos = [['pedro',[10,8],media]]
alunos = list()
contador = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome,[nota1,nota2],media])
    contador += 1
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    if resp in 'NNAONÃO':
        print('='*30)
        print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
        print('='*30)
        for n, a in enumerate(alunos):
            print(f'{n:<4}{alunos[n][0]:<10}{alunos[n][2]:>8.2f}')
        break

while True:
    print('-'*30)
    opc = int(input('Ver notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Volte sempre!')
        break
    if 0 <= opc < len(alunos):
        print(f'Notas de {alunos[opc][0]}: {alunos[opc][1]}')
    else:
        print('Não tem aluno cadastrado nesse valor')

    