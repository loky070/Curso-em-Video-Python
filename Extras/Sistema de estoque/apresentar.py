LIMITE_MIN = {
    "bola": 5,
    "tenis": 2,
    "camisa": 10,
    "acessorio": 3
}

LIMITE_MAX = {
    "bola": 50,
    "tenis": 20,
    "camisa": 100,
    "acessorio": 30
}

usuarios = [
    {"codigo": 1, "nome": "Admin", "senha": "123"}
]
usuario_logado = ""

produtos = [{'codigo': 1, 'nome': 'carlos', 'categoria': 'camisa', 'quantidade': 23, 'preco': 100.0}]

def mostrar_produtos(produtos):
    for p in produtos:
        print(
            f"Código: {p['codigo']}\n"
            f"Nome: {p['nome']}\n"
            f"Categoria: {p['categoria']}\n"
            f"Quantidade: {p['quantidade']}\n"
            f"Preço: R${p['preco']:.2f}\n{'-' * 30}"
        )

#sistema de login

login_realizado = False

while not login_realizado:
    print('-' * 30)
    usuario = input('Digite o seu usuário:\n').strip()
    senha = input('Digite a senha:\n').strip()

    for u in usuarios:
        if u["nome"] == usuario and u["senha"] == senha:
            print('Login realizado com sucesso!')
            print('-' * 30)
            login_realizado = True
            usuario_logado = usuario
            break
    else:
        print(f'Usuário ou senha incorretos\n{'-' * 30}')


while True:

    print('Bem vindo à Vest Sport!\nOs melhores compram aqui !\n')

    comando = input('\nEscolha a opção abaixo:\n'+
                    '[1] Cadastrar produto\n'+ #feito
                    '[2] Editar produtos\n'+ #feito
                    '[3] Deletar produtos\n'+ #feito
                    '[4] Cadastrar usuário\n'+ #feito
                    '[5] Mostrar quantidade de produtos\n'+ #feito
                    '[6] Venda de produtos\n'+ #feito
                    '[7] Terminar programa\n').strip() #feito
    match comando:
        case '1':
            print(f"{'-' * 30}\nCadastro de produto")
            codigo = len(produtos) + 1
            nome = input('Nome do produto:\n').strip().lower()
            categoria = input('Categoria (bola/tenis/camisa/acessorio):\n').lower().strip()


            if categoria not in LIMITE_MIN:
                print(f"Categoria inválida!\n{'-' * 30}")
                continue

            quantidade = int(input('Quantidade do produto:\n'))

            # Valida quantidade mínima/máxima individual
            if quantidade < LIMITE_MIN[categoria]:
                print(f"Quantidade mínima para {categoria}: {LIMITE_MIN[categoria]}\n{'-' * 30}")
                continue

            # Valida quantidade máxima considerando o estoque já existente
            quantidade_atual_categoria = sum(p['quantidade'] for p in produtos if p['categoria'] == categoria)
            if quantidade_atual_categoria + quantidade > LIMITE_MAX[categoria]:
                print(f"Não é possível adicionar {quantidade} {categoria}(s).")
                print(f"Estoque máximo permitido: {LIMITE_MAX[categoria]}")
                print(f"Quantidade atual em estoque: {quantidade_atual_categoria}\n{'-' * 30}")
                continue

            preco = float(input("Preço unitário (R$): "))

            produtos.append({
                "codigo": codigo,
                "nome": nome,
                "categoria": categoria,
                "quantidade": quantidade,
                "preco": preco
            })

            print(f"Produto cadastrado com sucesso!\n{'-' * 30}")

        case '2':
            print(f'{'-' * 30}\nEdição de produto')

            mostrar_produtos(produtos)

            codigo = int(input("Digite o código do produto: "))
            for p in produtos:
                if p["codigo"] == codigo:
                    p["nome"] = input("Novo nome: ").strip().lower()
                    p["categoria"] = input("Nova categoria: ").strip().lower()
                    p["quantidade"] = int(input("Nova quantidade: "))
                    p["preco"] = float(input("Novo preço: "))
                    print(f"Produto atualizado com sucesso!\n{'-' * 30}")
                    continue
            print(f"Produto não encontrado.\n{'-' * 30}")
        case '3':
            print('-' * 30)
            print("Deleção de produto")

            # Mostrar lista de produtos
            if not produtos:
                print(f"Não há produtos cadastrados.\n{'-' * 30}")
                continue

            print("Produtos cadastrados:")
            mostrar_produtos(produtos)

            # Perguntar qual produto deletar
            codigo_deletar = int(input("Digite o código do produto que deseja deletar: "))

            for p in produtos:
                if p["codigo"] == codigo_deletar:
                    produtos.remove(p)
                    print(f"Produto '{p['nome']}' deletado com sucesso!\n{'-' * 30}")
                    break
            else:
                print(f"Produto com código {codigo_deletar} não encontrado.\n{'-' * 30}")

        case '4':
            print(f"{'-' * 30}\nAdicionando novo usuário\n")
            novo_usuario = input('Digite o nome do usuário:\n').strip().lower()
            nova_senha = input('Digite a nova senha:\n').strip()
            codigo = len(usuarios) + 1
            usuarios.append({"codigo": codigo, "nome": novo_usuario, "senha": nova_senha})
            print(f'\nUsuário cadastrado com sucesso!\nUsuário: {novo_usuario}\nSenha: {nova_senha}\n{'-' * 30}')

        case '5':
            print(f"{'-' * 30}\nRelatório de estoque")
            print(f"Usuário logado: {usuario_logado}\n")

            if not produtos:
                print("Não há produtos cadastrados.\n" + '-' * 30)
                continue

            total_qtd = sum(p['quantidade'] for p in produtos)
            total_valor = sum(p['quantidade'] * p['preco'] for p in produtos)

            print(f"Total de produtos: {total_qtd} | Valor total: R$ {total_valor:.2f}")

            categorias = {}
            for p in produtos:
                categorias[p['categoria']] = categorias.get(p['categoria'], 0) + p['quantidade']

            for cat, qtd in categorias.items():
                print(f"{cat.capitalize()}: {qtd} unidades ({qtd / total_qtd * 100:.1f}%)")

            print('-' * 30)

        case '6':
            print(f"{'-' * 30}\nVenda de produtos")

            # Mostra todos os produtos cadastrados
            if not produtos:
                print("Não há produtos cadastrados.\n" + '-' * 30)
                continue

            print("Produtos disponíveis:")
            for p in produtos:
                print(
                    f"Código: {p['codigo']} | Nome: {p['nome']} | Categoria: {p['categoria']} | Quantidade: {p['quantidade']} | Preço: R${p['preco']:.2f}")

            # Seleciona o produto
            codigo_venda = int(input("Digite o código do produto para venda: "))

            # Procura o produto pelo código
            for p in produtos:
                if p['codigo'] == codigo_venda:
                    # Pergunta a quantidade a vender
                    quantidade_vender = int(input(f"Quantos(as) {p['categoria']} deseja vender? "))

                    # Verifica se há estoque suficiente

                    if quantidade_vender > p['quantidade']:
                        print(f"Estoque insuficiente! Apenas {p['quantidade']} disponível.\n{'-' * 30}")

                    else:
                        p['quantidade'] -= quantidade_vender
                        print(
                            f"Venda realizada: {quantidade_vender} {p['quantidade']} vendidos.\nQuantidade restante: {p['quantidade']}\n{'-' * 30}")
                    break
            else:
                print(f"Produto com código {codigo_venda} não encontrado.\n{'-' * 30}")

        case '7':
                print('Finalizando programa...')
                break
                
        case _:
            print(f"\nComando inválido, tente novamente.\n{'-' * 30}")
        