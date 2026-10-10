peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('\033[36mVocê está ABAIXO DO PESO, coma mais!\033[m')
elif 18.5 <= imc < 25:
    print('\033[32mParabéns! Você está no PESO IDEAL.\033[m')
elif 25 <= imc < 30:
    print('\033[33mVocê está com SOBREPESO, fique atento!\033[m')
elif 30 <= imc < 40:
    print('\033[31mVocê já está com OBESIDADE! Cuidado!\033[m')
elif imc >= 40:
    print('\033[1;31mVocê está com OBESIDADE MÓRBIDA!!!!! Procure ajuda agora!\033[m')