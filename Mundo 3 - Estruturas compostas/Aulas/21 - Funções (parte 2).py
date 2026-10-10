# ex101------------ex106

def mostralinha():
        print("----------")

def mensagem(msg):
        print("="*30)
        print(msg)
        print("="*30)
        
mensagem("SISTEMA DE ALUNOS")

def separar():
    print()
    print("="*30)
    print()

#DOCSTRING
def contador(i, f, p):
    """
    ->Faz uma contagem e mostra na tela
    -Parâmetro i: início da contagem
    -Parâmetro f: fim da contagem
    -Parâmetro p: passo da contagem
    -return: sem retorno
    Função criada para estudos.

    """
    c = i
    while c <= f:
        print(f"{c}",end="...")
        c += p
    print("FIM!")


contador(1,20,2)
separar()
help(contador)

separar()

#Parâmetros Opcionais
def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f"A soma vale {s}")

somar(5,6,7)
somar(5,6)
somar(5)
somar()
#da pra fzr fora de ordem tbm
somar(c=5,a=3)

separar()

# finge q é outro arquivo a partir daki


#Escopo de Variável 
#a var "b" dentro da função é uma variável local, tem escopo local
def teste(b):
    # as alterações da variável afetam globalmente, mesmo estando local
    global c
    #esse "a", mesmo existindo fora, a gente definiu que dentro da def ele recebe 8,
    #então ele vai ser uma var local
    a = 8
    b += 4
    c = 7
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

#Programa Principal

#a var "a" é uma variável global, tem escopo global
a = 5
c = 2
teste(a)
print(f"A fora vale {a}")
print(f"C fora vale {c}")


separar()

#Retorno de Valores

def somarDenovo(a=0,b=0,c=0):
    s = a+b+c
    return s

retorno = somarDenovo(3,7,2)
print(retorno)
#ou
print(somarDenovo(6,2,8))

#é interessante pra fazer coisas do tipo:

r1 = somarDenovo(4,2)
r2 = somarDenovo(5,1,8)
r3 = somarDenovo(3,6,9)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')

separar()

#Parte prática(sim, só agora q é a parte prática...)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = 5
print(f'O fatorial de {n} é {fatorial(n)}')

f1 = fatorial(6)
f2 = fatorial(0)
f3 = fatorial(12)
f4 = fatorial(4)
print(f'Os resultados são {f1}, {f2}, {f3} e {f4}')

def par(n=0):
    return True if n % 2 == 0 else False

def partambemmasagentenãovaiusarmasébomsaber(n=0):
    return n % 2 == 0

print(par(100))
print(par(75))
print(par(2))
print(par(3))