try:
    # tenta
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

# os except checam do primeiro ao último
except (ValueError, TypeError):
    print('Tivemos problema com os tipos de dados que você digitou')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')

except Exception as erro:
    # se der erro
    # pode ter mais que um "except"
    # o "Exception" transforma o erro numa variável
    print(f'O erro encontrado foi: {erro.__cause__}')
    
else:
    # opcional
    # se não der erro
    print(f'O resultado é {r:.2f}')

finally:
    # opcional
    # se der certo ou errado
    print('Volte sempre!')