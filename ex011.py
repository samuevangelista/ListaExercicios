print('Vamos pintar uma parede!')
a = float(input('Digite a altura da parede desejada: '))
l = float(input('Agora digite a largura da mesma: '))
area = a * l
tinta = area / 2
print('Sabemos que a parede tem {}m² de area, logo, teremos que usar {} litros de tinta para pintala'.format(area, tinta))
