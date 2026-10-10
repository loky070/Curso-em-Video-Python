while True:
    print(f'{"LOJA LOKY":=^40}')
    compra = float(input('Preço das compras: R$'))
    escolha = int(input('''
    FORMA DE PAGAMENTO
    [1] À vista dinheiro/cheque
    [2] À vista cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão
    Qual sua opção? 
    '''))
    if escolha == 1:
        final = compra * 0.9
    elif escolha == 2:
        final = compra * 0.95
    elif escolha == 3:
        final = compra
        parcela = compra / 2
        print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
    elif escolha == 4:
        final = compra * 1.2
        total_parcela = int(input('Quantas vezes quer parcelar? '))
        parcela = final / total_parcela
        print(f'Sua compra será parcelada em {total_parcela}x de R${parcela:.2f} COM JUROS')
    else: 
        print('OPÇÃO INVÁLIDA, tenta novamente...')
        continue
        
    print(f'Sua compra de R${compra:.2f} irá custar R${final:.2f}')
    break