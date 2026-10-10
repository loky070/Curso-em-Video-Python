def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :para n: O número a ser calculado.
    :para show: (opcional) mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """

    f = 1
    for x in range(n, 0, -1):
        if show:
            print(x,end='')
            if x > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= x
    return f


print(fatorial(5,show=True))
print(fatorial(5,show=False))

help(fatorial)