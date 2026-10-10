largura = float(input('Largura: '))
altura = float(input('Altura: '))

area = largura * altura
tinta = area / 2

print(f'Uma parede de {largura} x {altura} tem área de {area} m².'
      f'Você precisará de {tinta:.1f}l de tinta.')

