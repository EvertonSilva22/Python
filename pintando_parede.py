Largura = float(input('Qual a largura da parede? '))
Altura = float(input('Qual a altura da parede? '))
Total = Largura * Altura
Tinta = Total /2

print('A sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m2'.format(Largura, Altura, Total))
print('Para pintar sua parede, você presisará de {:.2f}l de tinta.'.format(Tinta))