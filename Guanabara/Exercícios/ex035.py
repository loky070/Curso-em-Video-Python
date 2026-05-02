a = float(input('\033[30;44mDigite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if a<b+c and b<a+c and c<a+b:
    print('\033[;32mA figura pode formar um triângulo.\033[m')
else:
    print('\033[;31mA figura NÃO pode formar um triângulo\033[m')


