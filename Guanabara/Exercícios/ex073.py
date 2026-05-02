times_brasileirao = (
    "Botafogo", "Chapecoense", "Vitória", "Fluminense", "Mirassol",
    "Bahia", "São Paulo", "Athletico-PR", "Bragantino", "Palmeiras",
    "Atlético-MG", "Flamengo", "Grêmio", "Corinthians", "Vasco da Gama",
    "Coritiba", "Internacional", "Santos", "Remo", "Cruzeiro"
)
for t in times_brasileirao:
    print(t, end='\n')

print(f'\nOs 5 primeiros são: {times_brasileirao[:5]}')

print(f'\nOs 4 últimos são {times_brasileirao[-4:]}')

print('\nTimes em ordem alfabética: ')
for t in range(0,len(times_brasileirao)):
    print(f'{sorted(times_brasileirao)[t]}')

print(f'O Chapecoense está na {times_brasileirao.index('Chapecoense') + 1}?° posição')