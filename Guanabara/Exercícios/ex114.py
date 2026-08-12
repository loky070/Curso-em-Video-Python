import requests

try:
    site = requests.get('http://www.pudim.com.br')
    site.raise_for_status()

except requests.exceptions.RequestException:
    print('O site não está acessível.')

else:
    print('Consegui acessar!')
    conteudo = site.text

    print(conteudo)


# não sei pq mas não tá funfando esse código do guanabara, mas com a outra biblioteca tá funfando dboa

# import urllib
# import urllib.request

# try:
#     site = urllib.request.urlopen('http://www.pudim.com.br')
# except:
#     print('Deu erro...')
# else:
#     print('DEU CERTO')