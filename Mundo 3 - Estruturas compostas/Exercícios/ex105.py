def notas(*notas,situacao=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :para notas: uma ou mais notas dos alunos(aceita várias)
    :para situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    
    avaliacao = dict()
    avaliacao['total'] = len(notas)
    avaliacao['maior'] = max(notas)
    avaliacao['menor'] = min(notas)
    media = sum(notas)/len(notas)
    avaliacao['media'] = media

    if situacao:
        if media >= 7:
            avaliacao['situação'] = 'BOA'
        elif media >= 5:
            avaliacao['situação'] = 'RAZOÁVEL'
        else:
            avaliacao['situação'] = 'RUIM'
    return avaliacao

resposta = notas(5.5, 9.5, 10, 6.5, situacao=True)
resposta2 = notas(5)
resposta3 = notas(1, situacao=True)
print(resposta)
print(resposta2)
print(resposta3)

help(notas)
