import math

ang = float(input('Digite o ângulo: '))

seno = math.sin(math.radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')

cosseno = math.cos(math.radians(ang))
print(f'O ângulo de {ang} tem o COSSENO de {cosseno:.2f}')

tangente = math.tan(math.radians(ang))
print(f'O ângulo de {ang} tem a TANGENTE de {tangente:.2f}')
