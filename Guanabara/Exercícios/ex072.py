numeros = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    entrada = input('Digite um número entre 0 e vinte: ').strip()
    if entrada.isdigit():
        escolha = int(entrada)
        if  0<= escolha <= 20 :
            break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {numeros[escolha]}')