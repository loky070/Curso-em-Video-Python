velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\033[31mVocê foi multado por excesso de velocidade em {multa:.2f} reais.\033[m')
else:
    print('\033[034mO limite de velocidade não foi atingido, sem multa.\033[m')