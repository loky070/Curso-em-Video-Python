a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if a<b+c and b<a+c and c<a+b:
    print('\033[;32mA figura pode formar um triângulo.\033[m')
    if a == b == c:
        print('É um triângulo Equilátero, todos os lados são iguais.')
    elif a == b or b == c or a == c:
        print('É um triângulo Isósceles, dois lados são iguais.')
    else:
        print('É um triângulo Escaleno, todos os lados são diferentes.')
else:
    print('\033[;31mA figura NÃO pode formar um triângulo\033[m')
#guanaba fez diferente mas igual, mas eu prefiro o meu. Mas só pra deixar comentado...
#ele usa o final com end='' e continua só com a fala de qual tipo é.